import pandas as pd 
import matplotlib.pyplot as plt

# leer csv 
csv= pd.read_csv('.\MATPLOTLIB\cwurData.csv', sep=',',decimal='.')
#print(csv)

dataframe=csv[['institution', 'publications', 'influence']].head()
print(dataframe)

plt.scatter(dataframe['institution'], dataframe['publications'],label="Publicacion",marker='*')
plt.step(dataframe['institution'],dataframe['influence'],label="Influencia",linestyle='--',marker='o')
plt.xticks(dataframe['institution'],rotation=10,ha='right',fontsize=7)
plt.title("POSICION POR PUBLICACIONES E INFLUENCIA")
plt.legend()
plt.grid(linewidth=1.5,alpha=0.25)
plt.show()