from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy 

web='https://demo.scrapingbee.com/table_content.html'

#peticiones http
response=requests.get(web)
content=(response.text)
#print(content)

#analizar - parser
soup=BeautifulSoup(content,'lxml')
data=soup.find_all('tr',valign='middle')
#print(data)

#arreglos
symbol=[]
name=[]
price=[]
change=[]
p_change=[]

#recorrido
for d in data:
    symbol.append(d.find('td',class_='symbol').find('a').get_text())
    name.append(d.find('td',class_='name').get_text())
    price.append(d.find('td',class_='unchanged numData').get_text())
    change.append(d.find('td',class_=('quoteDecline','quoteGain')).get_text())
    p_change.append(d.find('td',class_=('quoteDecline','quoteGain')).find_next("td").get_text().strip())

etiquetas_data={'Abreviatura':symbol, 'Nombre':name, 'Precio':price, 'Cambio':change , 'Porcentaje_cambio':p_change}
dataframe=pd.DataFrame(etiquetas_data)
print(dataframe)

# conexion bd
database_username='root'
database_password='12345678'
database_ip='127.0.0.1'
database_name='prueba'
database_connection=sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                             format(database_username,database_password,database_ip,database_name))

dataframe.to_sql(con=database_connection,name='dataframe_mysql',if_exists='replace',index=True)
print('LA TABLA HA SIDO CREADA CORRECTAMENTE')
