import mysql.connector 
import pandas as pd

#conexion bd
conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='prueba'
)
#prueba de conexion
data2=pd.read_sql("SELECT * FROM personas",conexion)
print(data2)

#eliminar fila
print(data2.drop([1,3]))

#agregar fila
print("================================================")
df=data2._append({'id':501,'firstname':'Luis','lastname':'Ochoa','email':'luisochoa@gmail.com'},ignore_index=True)
print(df)  
print("================================================")
print(df[(df['firstname']=='Luis')]) 
print("================================================")
print(df.sort_values('firstname',ascending=True))


