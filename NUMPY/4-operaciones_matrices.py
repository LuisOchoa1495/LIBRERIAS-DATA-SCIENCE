import numpy as np
#producto de dos vectores
v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(v1@v2)
print(v1.dot(v2))

#producto de dos matrices
m1=np.array([[1,2,3],[4,5,6]])
m2=np.array([[1,1],[2,2],[3,3]])
print(m1@m2)
print(m1.dot(m2))

#modulo de un vector
m=np.array([3,4])
print(np.linalg.norm(m))

#traspuesta
print("Traspuesta: " + str(m1.T))
#traza 
m3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Traza: "+str(m3.trace()))

#determinante
d=np.array([[1,2],[3,4]])
print("Determinante: "+str(np.linalg.det(d)))

#matriz inversa
print("Matriz Inversa: "+str(np.linalg.inv(d)))