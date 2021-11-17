import numpy as np
def getTensorDot():

    a = np.arange(60.).reshape(3,4,5)
    b = np.arange(24.).reshape(4,3,2)
    c = np.tensordot(a,b, axes=([1,0],[0,1]))

    print(a)
    print(b)
    print(c)
    d = np.zeros((5,2))
    for i in range(5):
        for j in range(2):
            for k in range(3):
                for n in range(4):
                    d[i,j] += a[k,n,i] * b[n,k,j]
    print(d)


    print('=============================')
    a = np.array(range(1, 9))
    a.shape = (2, 2, 2)
    A = np.array(('a', 'b', 'c', 'd'), dtype=object)
    A.shape = (2, 2)
    print('a:')
    print(a)
    print('A:')
    print(A)

    print('np.tensordot(a, A)')
    print(np.tensordot(a, A)) # third argument default is 2 for double-contraction
    print('np.tensordot(a, A, 1)')
    print(np.tensordot(a, A, 1))
    print('np.tensordot(a, A, 0)')
    print(np.tensordot(a, A, 0))
    print('np.tensordot(a, A, (0, 1))')
    print(np.tensordot(a, A, (0, 1)))
    print('np.tensordot(a, A, (2, 1))')
    print(np.tensordot(a, A, (2, 1)))
    print('np.tensordot(a, A, ((0, 1), (0, 1)))')
    print(np.tensordot(a, A, ((0, 1), (0, 1))))
    print('np.tensordot(a, A, ((2, 1), (1, 0)))')
    print(np.tensordot(a, A, ((2, 1), (1, 0))))
    print('===========')
