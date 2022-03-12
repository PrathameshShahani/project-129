import csv
import pandas as pd

df=pd.read_csv("dwarf_stars.csv")
print(df.columns)

df=df.dropna()
print(df.dtypes)

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df['Radius']=0.102763*df['Radius']
df['Mass']=0.000954588*df['Mass']

df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df.columns)

df.to_csv("converted.csv")