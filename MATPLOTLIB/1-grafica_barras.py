import pandas as pd 
import matplotlib.pyplot as plt

# leer csv 
csv= pd.read_csv('.\MATPLOTLIB\cwurData.csv', sep=',',decimal='.')
#print(csv)
dataframe=csv[['institution', 'score']]
print(dataframe)
institute=csv['institution'].head()
score=csv['score'].head()
print(institute)
print(score)

#grafica
plt.bar(institute,score,edgecolor='black',width=0.5)
#etiqueta
for i in range(len(score)):
    plt.text(i,score[i],score[i],ha='center',size=8)

plt.yticks(fontsize=8)
plt.xticks(fontsize=7.2,rotation=10,ha='right')
plt.title("TOP 5 INSTITUTE - SCORE")
plt.show()