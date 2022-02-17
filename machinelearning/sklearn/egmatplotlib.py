import matplotlib.pyplot as plt
import numpy as np

f = []

#x1+x2-5 >=0
g1=[]
x=[]
for i in range(-1,6,1):
    x.append(i)
    g1.append(5-i)

circleX=[]
yUp=[]
yDown=[]

fUp1=[]
fDown1=[]

fUp2=[]
fDown2=[]

fUp3=[]
fDown3=[]

fUp4=[]
fDown4=[]

fUp5=[]
fDown5=[]
for i in np.arange(-8,8,0.0001):
    circleX.append(i)
    yDown.append(2.5 - np.sqrt(25/4 - i))
    yUp.append(2.5 + np.sqrt(25/4 - i))

    fUp1.append(1+np.sqrt(1-(i-2)**2))
    fDown1.append(1-np.sqrt(1-(i-2)**2))

    fUp2.append(1+np.sqrt(2-(i-2)**2))
    fDown2.append(1-np.sqrt(2-(i-2)**2))

    fUp3.append(1+np.sqrt(4-(i-2)**2))
    fDown3.append(1-np.sqrt(4-(i-2)**2))

    fUp4.append(1+np.sqrt(12-(i-2)**2))
    fDown4.append(1-np.sqrt(12-(i-2)**2))

    fUp5.append(1+np.sqrt(20-(i-2)**2))
    fDown5.append(1-np.sqrt(20-(i-2)**2))


plt.plot(circleX,yDown,c='cornflowerblue')
plt.plot(circleX,yUp,c='cornflowerblue')
plt.plot(circleX,fUp1,c='tomato')
plt.plot(circleX,fDown1,c='tomato')

plt.plot(circleX,fUp2,c='tomato')
plt.plot(circleX,fDown2,c='tomato')

plt.plot(circleX,fUp3,c='tomato')
plt.plot(circleX,fDown3,c='tomato')

plt.plot(circleX,fUp4,c='tomato')
plt.plot(circleX,fDown4,c='tomato')

plt.plot(circleX,fUp5,c='tomato')
plt.plot(circleX,fDown5,c='tomato')

plt.plot(x,g1,c='limegreen')

plt.axhline(0,c='b')
plt.axvline(0,c='b')

plt.axhline(1,c='peru',linestyle='-.')
plt.axvline(4,c='peru',linestyle='-.')

plt.show()