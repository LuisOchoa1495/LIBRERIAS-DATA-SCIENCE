import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.Series([1,2,3,4,5,6,7,8,9,10])
df2=pd.Series(np.power(df,2))
print(df2)
df3=pd.Series(np.power(df,3))

plt.plot(df,df2,label="potencia 2")
plt.plot(df,df3,label="potencia 3")
plt.xticks(df)
plt.legend()
plt.show()