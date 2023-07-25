import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')

pi = np.linspace(0, np.pi,50)

malha = np.meshgrid(pi,pi)
eixoZ = np.sin(malha[0])*np.sin(malha[1])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
area = ax.plot_surface(malha[0],malha[1],eixoZ, cmap=cm.hsv)
plt.show()