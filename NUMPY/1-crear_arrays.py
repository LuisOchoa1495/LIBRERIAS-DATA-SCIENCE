import numpy as np

#Array de una dimension
a1=np.array([1,2,3])
print(a1)

#Array de dos dimensiones
a2=np.array([[1,2,3],[4,5,6]])
print(a2)

#Array de tres dimensiones
a3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3)

print("================================================")
#identity
i=np.identity(3)
print(i)

zero=np.zeros((2,3))
print(zero)

range=np.arange(2,15,2)
print(range)

diag=np.diag([3,5,7,9])
print(diag)

random=np.random.random((3,4))
print(random)

randomInt=np.random.randint(-5,12,(4,4))
print(randomInt)