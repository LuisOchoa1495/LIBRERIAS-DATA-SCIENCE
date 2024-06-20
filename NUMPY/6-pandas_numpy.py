import pandas as pd
import numpy as np

s=pd.Series(['a', 'b', None, 'c', np.NaN, np.sin(45),np.tan(45)])
print(s)

#eliminar datos desconocidos o nulos
print(s.dropna())