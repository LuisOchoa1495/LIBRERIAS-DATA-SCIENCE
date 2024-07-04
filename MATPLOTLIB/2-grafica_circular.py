import pandas as pd 
import matplotlib.pyplot as plt

# leer csv 
csv= pd.read_csv('.\MATPLOTLIB\cwurData.csv', sep=',',decimal='.')
print(csv)

country=csv[['country']]
print(country)
df=country.value_counts().head()
df=df.reset_index()
df.columns=['country', 'total']
print(df)

plt.pie(df['total'],labels=df['country'],autopct='%1.1f%%')
plt.title("PORCENTAJE DE UNIVERSIDADES POR EL MUNDO - TOP5")
plt.show()