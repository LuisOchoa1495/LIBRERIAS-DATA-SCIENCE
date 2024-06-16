import pandas as pd 
#serie
s=pd.Series({'Algoritmos':6.0,'Base de datos':4.5, 'Programacion':8.5,'Redes de computadoras':5})
print(s)
print('Longitud de serie:'+str(s.size))
print(s['Algoritmos'])

print('================================================================')
print(s.min())
print(s.max())
print(s.sum())
print(s.count())

print('==========================DESCRIPCION======================================')
print(s.describe())