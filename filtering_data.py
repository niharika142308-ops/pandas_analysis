#import library
import pandas as pd
#reading the data
import re 
df = pd.read_csv('pokemon_data.csv')
#ignore case
print(df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)])
#starts with pi
print(df.loc[df['Name'].str.contains('^pi[A-Z]*',flags=re.I,regex=True)])

#conditional changes
# df.loc[df['Type 1']=='Flamer','Type 1']='Fire'
# print(df)

df.loc[df['Type 1']=='Fire','Legendary']='True'
print(df)
df=pd.read_csv('modified.csv')
print(df)

# df.loc[df['Total']>500,['Generation','Legendary']]=['Test value',1]
# print(df)

#aggregating 
print(df.groupby(['Type 1']).mean())

print(df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False))

print(df.groupby(['Type 1']).mean().sort_values('Attack',ascending=False))

print(df.groupby(['Type 1']).sum())

print(df.groupby(['Type 1']).count())


#cleaning output
df=pd.read_csv('modified.csv')
df['count']=1
print(df.groupby(['Type 1']).count()['count'])