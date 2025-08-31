import pandas as pd


df = pd.DataFrame(columns=['x', 'y', 'z'])

df.loc[0] = [1,2,None]
df.loc[:,'z'] = df.loc[:,'x']*df.loc[:,'y']

print(df)