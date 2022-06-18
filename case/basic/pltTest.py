import matplotlib.pyplot as plt
y1=[]
y2=[]
x=[]
for i in range(1,800):
    x.append(i)
    y1.append(240-0.5*i)
    y2.append(300-i)

plt.plot(x,y1,c='cornflowerblue')
plt.plot(x,y2,c='peru')
plt.axvline(200,c='limegreen')
plt.xlim(0,500)
plt.ylim(0,300)
plt.text(121,181,'(120,180)')
plt.text(201,140,'(200,140)')
plt.text(201,100,'(200,100)')
plt.show()