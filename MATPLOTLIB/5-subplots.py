import pandas as pd 
import matplotlib.pyplot as plt

# leer csv 
csv= pd.read_csv('.\MATPLOTLIB\cwurData.csv', sep=',',decimal='.')
print(csv)

#------plot 1
institute=csv['institution'].head()
score=csv['score'].head()
plt.subplot(2,2,1)
#grafica
plt.bar(institute,score,edgecolor='black',width=0.5)
#etiqueta
for i in range(len(score)):
    plt.text(i,score[i],score[i],ha='center',size=8)

plt.yticks(fontsize=8)
plt.xticks(fontsize=7.2,rotation=10,ha='right')
plt.title("TOP 5 INSTITUTE - SCORE")

#-----plot 2
country=csv[['country']]
df=country.value_counts().head()
df=df.reset_index()
df.columns=['country', 'total']
plt.subplot(2,2,2)
plt.pie(df['total'],labels=df['country'],autopct='%1.1f%%')
plt.title("PORCENTAJE DE UNIVERSIDADES POR EL MUNDO - TOP5")

#------plot 3
dataframe=csv[['institution', 'quality_of_education','quality_of_faculty']].head()
plt.subplot(2,2,3)
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

#------plot 4
dataframe2=csv[['institution', 'publications', 'influence']].head()
print(dataframe2)
plt.subplot(2,2,4)
plt.scatter(dataframe2['institution'], dataframe2['publications'],label="Publicacion",marker='*')
plt.step(dataframe2['institution'],dataframe2['influence'],label="Influencia",linestyle='--',marker='o')
plt.xticks(dataframe['institution'],rotation=10,ha='right',fontsize=7)
plt.title("POSICION POR PUBLICACIONES E INFLUENCIA")
plt.legend()
plt.grid(linewidth=1.5,alpha=0.25)

#----------------------------------------------------
plt.suptitle("RANKING UNIVERSIDADES 2012",fontsize=15,style='italic')
plt.subplots_adjust(hspace=0.4)
plt.show()