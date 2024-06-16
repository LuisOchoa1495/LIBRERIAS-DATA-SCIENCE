import pandas as pd
#operaciones
s1=pd.Series([1,2,3,4,5,6,7,8,9])
s2=pd.Series(['a', 'b', 'c', 'd', 'e', 'f'])

print('===========================OPERACIONES=====================================')
print(s1*4)
print('------------------------------------------------')
print(s2*3)

#filtros
s=pd.Series({'Algoritmos':6.0,'Base de datos':4.5, 'Programacion':8.5,'Redes de computadoras':5})
print('===========================FILTROS================================')
print(s[s>5])

#orden
print('===========================ORDENAMIENTO=====================================')
print(">>Orden values:")
print(s.sort_values(ascending=True))
print('------------------------------------------------')
print(">>Orden index:")
print(s.sort_index(ascending=False))