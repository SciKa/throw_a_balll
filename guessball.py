import numpy as np
import sympy as sp

a,b = map(float,input("타격 목표 지점을 입력하세요, x(공백)y :").split(" "))
vmax = float(input("검사할 발사 속력 상한을 입력하세요. 입력한 속력값까지 조금씩 속력을 늘려가며 검사해, 발사각 해가 있는지 따져봅니다. :"))
vf = int(input("0부터 방금 입력한 발사 속력 상한까지 몇등분하여 검사할 지 입력하세요. 클수록 정밀해지지만 느려집니다. 정수 입력. :"))

test_vec = np.linspace(0,vmax,vf)
j = 0
while True:
    # 초기값 설정
    init_pos = np.array([0, 0])
    target_pos = np.array([a, b])
    init_vel_size = test_vec[j]

    # theta 구하기
    theta = sp.symbols("theta")
    x = target_pos[0]
    y = target_pos[1]
    v0 = init_vel_size
    f = -y + sp.sin(theta) / sp.cos(theta) * x - (9.80665 * x ** 2) / (2 * v0 ** 2 * sp.cos(theta) ** 2)
    solve = sp.solve(f)

    # 실수화, ndarray화, 음의 해 제외
    solve_r = []
    for i in solve:
        if i.is_real == True and i > 0:
            solve_r.append(i)
    solve_r = np.array(solve_r)
    if solve_r.size == 0:
        print("v_0 = {0} 에선 유의미한 발사각도 해가 없습니다.".format(init_vel_size))
        j += 1
    else:
        print("한계값 발견! v_0 = {0} 이상부터 발사각도 해가 존재합니다.".format(init_vel_size))
        break
v = float(input("발사 초기속력 값을 위의 한계값을 참조하여 입력하여 주세요. 실수 :"))

#초기값 설정
init_pos = np.array([0,0])
target_pos = np.array([a,b])
init_vel_size = v

#theta 구하기
theta = sp.symbols("theta")
x = target_pos[0]
y = target_pos[1]
v0 = init_vel_size
f = -y + sp.sin(theta)/sp.cos(theta)*x - (9.80665 * x**2) / (2 * v0**2 * sp.cos(theta)**2)
solve = sp.solve(f)

#실수화, ndarray화, 음의 해 제외
solve_r = []
for i in solve:
    if i.is_real == True and i > 0:
        solve_r.append(i)
solve_r = np.array(solve_r)
if solve_r.size == 0:
    print("아이쿠, 유의미한 해가 없습니다.")

#라디안>>도

print("각도 : ")
print(solve_r / np.pi * 180)
print("곧 포물선의 방정식 그래프가 나옵니다...윗쪽의 버튼을 이용하여 축척을 조정하세요.")

#시뮬레이션
def simulate(theta):
    x = sp.symbols("x")
    f = sp.sin(theta)/sp.cos(theta)*x - (9.80665 * x**2) / (2 * v0**2 * sp.cos(theta)**2)
    pl = sp.plot(f)

for theta in solve_r:
    simulate(theta)
