import numpy as np
import matplotlib.pyplot as plt

pos = np.array([0,0])
vel = np.array([0,0])
acc = np.array([0,0])

simul_t_range = np.linspace(0,10,1000)
simul_posx = np.array([])
simul_posy = np.array([])

init_pos = np.array([0,10])
init_vel = np.array([10,0])
init_acc = np.array([0,-9.8])

pos = pos + init_pos
vel = vel + init_vel
acc = acc + init_acc

i = 0
while True:
    timenow = 0
    timebefore = 0
    timedelta = 0
    if i == 0:
        timenow = simul_t_range[i]
        timebefore = None
        timedelta = None
    else:
        timenow = simul_t_range[i]
        timebefore = simul_t_range[i-1]
        timedelta = timenow - timebefore


    if timenow == 0.0:
        simul_posx = pos[0]
        simul_posy = pos[1]
    else:
        vel = vel + timedelta * acc
        pos = pos + timedelta * vel

        simul_posx = np.append(simul_posx,[pos[0]])
        simul_posy = np.append(simul_posy,[pos[1]])


    i += 1
    try:
        simul_t_range[i]
    except IndexError:
        break
print(simul_posx)
print(simul_posy)
plt.plot(simul_posx,simul_posy)
plt.show()