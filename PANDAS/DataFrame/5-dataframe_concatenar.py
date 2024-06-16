import pandas as pd
import mysql.connector
#>>>data frame1
data_frame1=pd.read_csv('.\PANDAS\data_prueba.csv',sep=',')

#>>>data frame2
#conexion bd
conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='prueba'
)
#prueba de conexion
data_frame2=pd.read_sql("SELECT * FROM personas",conexion)
data_frame2=data_frame2.rename(columns={'firstname' : 'first_name','lastname' : 'last_name'})
#imprimir
print(data_frame1)
print(data_frame2)

#df combinado 
df=pd.concat([data_frame1,data_frame2])
print(df)
#df  a csv 
df.to_csv('muestra.csv',index=False)


