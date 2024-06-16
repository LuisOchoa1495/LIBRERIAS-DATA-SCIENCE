import pandas as pd
df=pd.read_csv('.\PANDAS\data_prueba.csv',sep=',')
print(df.head())

#atributos
print('----------------------------------------------------------------')
print(df.info())

print('----------------------------------------------------------------')
print('Tamanio dataframe: '+str(df.shape))

print('----------------------------------------------------------------')
print(df.dtypes)