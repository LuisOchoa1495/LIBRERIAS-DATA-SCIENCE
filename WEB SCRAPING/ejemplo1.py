from bs4 import BeautifulSoup
import requests
import pandas as pd

web='https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
#hacer peticiones http 
response = requests.get(web)
content=(response.text)

# analizar - parser
soup=BeautifulSoup(content,'lxml')

matches=soup.find_all('div', class_='footballbox')

home = []
score=[]
away =[]
#recorrer - encontrar 
for match in matches:
    home.append(match.find('th', class_='fhome').get_text())
    score.append(match.find('th', class_='fscore').get_text())
    away.append(match.find('th', class_='faway').get_text())

mundial_2022={'local':home, 'marcador':score, 'visitante':away}
df_mundial_2022=pd.DataFrame(mundial_2022)
print(df_mundial_2022)