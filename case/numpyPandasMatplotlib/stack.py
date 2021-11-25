import numpy as np


A = np.ones((2, 2), int)
B = 2 * A

print(A)
print(B)

print('--np.hstack([A, B]) --')
x= np.hstack([A, B])
print(x.shape)


print('--np.vstack([A, B]) --')
A = np.ones((2, 2), int)
B = 2 * A
x= np.vstack([A, B])
print(x.shape)

print('--np.hstack([[A], [B]])--')
A = np.ones((2, 2), int)
B = 2 * A
x=np.hstack([[A], [B]])
print(x.shape)
print(x)

print('--np.vstack([[A], [B]])--')
A = np.ones((2, 2), int)
B = 2 * A

x=np.vstack([[A], [B]])
print(x.shape)
print(x)

print('--np.hstack([a, b]) --')
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
x= np.hstack([a, b])
print(x.shape)
print('--np.vstack([a, b]) --')
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
x= np.vstack([a, b])
print(x.shape)

print('--np.hstack([[a], [b]])--')
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
x= np.hstack([[a], [b]])
print(x.shape)

print('--np.vstack([[a], [b]])--')
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
x= np.vstack([[a], [b]])
print(x.shape)


