import numpy as np
#Array de dos dimensiones 
a2=np.array([[1,2,3],[4.5,5,6]])
print(a2)

#atributos de un array
print("Dimensiones: "+str(a2.shape))
print("Elementos: "+str(a2.size))
print("Tipo de dato: "+str(a2.dtype))

print("================================================================")
#acceso a elementos de un array
print(a2)
print(a2[1,2])
print(a2[:,0:2])