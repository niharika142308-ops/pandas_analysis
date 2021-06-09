import pandas as pd
df=pd.read_csv('modified.csv')
new_df=pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv',chunksize=5):
    result=df.groupby(['Type 1']).count()
    new_df=pd.concat([new_df,result])
print(new_df)    