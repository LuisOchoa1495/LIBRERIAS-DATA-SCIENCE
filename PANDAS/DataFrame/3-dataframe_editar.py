import pandas as pd
df=pd.read_csv('.\PANDAS\data_prueba.csv',sep=',')

# editar columnas
print(df.rename(columns={'first_name':'nombre', 'last_name':'apelldos'},index={0:1000,1:1001,2:1002}))

#reindexar elementos
print('================================================================')
print(df.reindex(index=[4,3,1],columns=['first_name','email']))

#acceso a elementos
print('================================================================')
print(df.loc[2,'last_name'])
print('----------------------------------')
print(df.loc[:3,'last_name'])
print('----------------------------------')
print(df['email'])