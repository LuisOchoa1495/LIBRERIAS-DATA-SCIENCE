import pandas as pd 
import matplotlib.pyplot as plt

#leer tablas 
tables=pd.read_html('https://www.nbamaniacs.com/palmares-nba/')
print(f'Numero de tablas: {len(tables)}')

#imprimir tablas
for i in range(len(tables)):
    print(tables[i])

#datos
datos=(tables[0])
print(datos)

#dataframe
dataframe=pd.DataFrame(datos[['Franquicia','Títulos']].head())
print(dataframe)

#grafica
dataframe.plot(x="Franquicia",kind="bar",rot=10)
plt.title("TOP 5 - CAMPEONES NBA")
plt.xticks(fontsize=9)
plt.show()

#guardar csv
datos.to_csv('ws_pandas.csv')