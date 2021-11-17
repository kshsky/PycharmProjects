import numpy as np
import matplotlib.pyplot as plt

a,stepA= np.linspace(0,10,num=5,endpoint=False,retstep=True)
print(a)
print(stepA)

print(np.linspace(0,10,num=5,endpoint=False,retstep=True))
b,stepB = np.linspace(0,10,num=5,endpoint=True,retstep=True)
print(b)
print(np.linspace(0,10,num=5,retstep=True))
print(stepB)

arr = np.arange(15).reshape((3, 5))
print(arr)

print(arr.T)
print(arr.swapaxes(1,0))