import unsio.input as uns_in 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.integrate as igr
import matplotlib.animation as animation

xmin = -8
ymin = xmin
xmax = -xmin
ymax = -xmin
simname="/home/elliot/runx.nemo" 
components="all" 
times="all" 
float32=True
fig, ax = plt.subplots()
plt.xlim(xmin,xmax)
plt.ylim(ymin, ymax)
SATXPOS = np.zeros(1000)
SATYPOS = np.zeros(1000)
PRIMXPOS = np.zeros(10000)
PRIMYPOS = np.zeros(10000)
sc = ax.scatter(SATXPOS, SATYPOS, c="r", s=5)
sc2 = ax.scatter(PRIMXPOS, PRIMYPOS, alpha=0.1, c="g", s=5)
my_in = uns_in.CUNS_IN(simname,"all","all",float32)


def animate(i):
    if my_in.nextFrame(""): 
        global PRIMXPOS, PRIMYPOS, SATXPOS, SATYPOS
        status,poss=my_in.getData("all","pos")
        status,timex=my_in.getData("time")
        possNew = np.reshape(poss, (-1, 3))
        SATXPOS = possNew[0:999, 0]
        SATYPOS = possNew[0:999, 1]
        PRIMXPOS = possNew[1000:10999, 0]
        PRIMYPOS = possNew[1000:10999, 1]
        sc2.set_offsets(np.c_[PRIMXPOS,PRIMYPOS])
        sc.set_offsets(np.c_[SATXPOS,SATYPOS])
        ax.set_title("Time = " + str(timex))

ani = animation.FuncAnimation(fig, animate, 
                frames=2000, interval=100, repeat=True) 

plt.show()
#new = np.reshape(a, (-1, ncols))

