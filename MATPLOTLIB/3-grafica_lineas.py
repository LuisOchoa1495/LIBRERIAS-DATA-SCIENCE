import pandas as pd 
import matplotlib.pyplot as plt

# leer csv 
csv= pd.read_csv('.\MATPLOTLIB\cwurData.csv', sep=',',decimal='.')
print(csv)

dataframe=csv[['institution', 'quality_of_education','quality_of_faculty']].head()
print(dataframe)

#grafica
plt.plot(dataframe['institution'], dataframe['quality_of_education'], label='CALIDAD DE EDUCACION',marker='o')
plt.plot(dataframe['institution'], dataframe['quality_of_faculty'], label='CALIDAD DE EDUCACION',marker='x')
#definir titulo y nombre de ejes
plt.title('POSICION POR CALIDAD DE EDUCACION - FACULTAD (TOP 5)')
plt.ylabel('Posicion')
plt.xticks(dataframe['institution'],rotation=10,ha='right',fontsize=7)
#mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()
