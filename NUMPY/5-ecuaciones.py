import numpy as np
#Sistema de dos ecuaciones y dos incognitas
#x+2y=1
#3x+5y=2
a=np.array([[1,2],[3,5]])
b=np.array([1,2])
print(np.linalg.solve(a,b))

#Sistema de dos ecuaciones y tres incognitas
#x+y+z=12
#2x-y+z=7
#x+2y-z=6
c=np.array([[1,1,1],[2,-1,1],[1,2,-1]])
d=np.array([12,7,6])
print(np.linalg.solve(c,d))
