import pandas as pd
#lista de diccionario
df=pd.DataFrame([{'Nombre':'Luis', 'Edad':28},
                 {'Nombre':'Jose', 'Edad':22},
                 {'Nombre':'Cristina', 'Edad':29}
                 ])
print(df)
print(df.max())
print(df.describe())

#diccionario de listas
print('================================================================')
datos={'nombre':['Maria', 'Luis', 'Carmen','Antonio'],
       'edad':[18,22,20,21],
       'grado':['Ecoonomia','Medicina','Arquitectura','Fisica'],
       'correo':['maria@gmail.com','luis@yahoo.es','carmen@gmail.com','antonio@gmail.com']
       }
df2=pd.DataFrame(datos)
print(df2)

#dataframe a partir de lista de listas
print('==================================================================')
df3=pd.DataFrame([['Maria',18],['Luis',22],['Carmen',20]],columns=['Nombre','Edad'])
print(df3)

