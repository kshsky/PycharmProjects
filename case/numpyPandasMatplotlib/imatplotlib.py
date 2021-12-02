import numpy as np
import matplotlib
import matplotlib.pyplot as plt
x = np.arange(0,1,0.00001)
y = np.log((1-x)/x)*0.5
plt.axvline(0.5,linestyle='-.',c='r')
plt.axhline(0,linestyle='--',c='m')
plt.text(0.5005,0.06,'(0.5,0)',fontdict={'fontsize':15})
plt.xlabel('error',fontdict={'fontsize':15})
plt.ylabel('0.5 * np.log((1-e)/e)',fontdict={'fontsize':15})
plt.plot(x,y)
plt.show()