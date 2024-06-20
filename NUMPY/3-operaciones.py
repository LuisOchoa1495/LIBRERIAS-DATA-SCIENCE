import numpy as np

v=np.arange(0,10)
print(v)

print(v*3)
print(v+7)
print(v-5)

v2=np.array([7,4,9,6,1,2,5,8,3,11])
print("================================================")
print("Suma: "+str(v+v2))
print("Division:"+str(v/v2))

#matriz
randomInt=np.random.randint(-5,12,(4,4))
print(randomInt)
print(randomInt-1)