#import library
import pandas as pd
#reading the data
df = pd.read_csv('pokemon_data.csv')
#print(df)
#printing first 5 rows 
#printing las rows using tail
#read excel data
# df_xls=pd.read_excel('pokemon_data.xlsx')
# print(df_xls.head(3))

print(df.head(5))
#Read headers 
print(df.columns)
#Read columns
print(df['Name'][0:5])
# or
#print(df.Name[0:5])
#Reading Multiple columns at the same time
print(df[['Name','Type 1','HP']])

#Read each row
print(df.iloc[1:4])

#Read a specific loaction(R,c)
print(df.iloc[2,1])


#iterating through each rows
# for index,row in df.iterrows():
#     print(index,row['Name'])

#finding specific data 
print(df.loc[df['Type 1']=='Fire'])

#describe data 
print(df.describe())

#sorting values
print(df.sort_values('Name',ascending=False))
print(df.sort_values(['Type 1','HP']))
print(df.sort_values(['Type 1','HP'],ascending=False))
print(df.sort_values(['Type 1','HP'],ascending=[1,0]))

#Making changes to data
#df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#to drop a column df=df.drop(columns=['Total'])
df['Total']=df.iloc[:,4:10].sum(axis=1)
#Reordering columns
cols=list(df.columns.values)
print(cols)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(5))

#to save data to csv
df.to_csv('modified.csv',index=False)
#to save in the form of excel need to install openpyxl
df.to_excel('modified.xlsx',index=False)
#save in the form of text
df.to_csv('modified.txt',index=False,sep='\t')

#Filtering the data 
print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')])
print(df.loc[(df['Type 1']=='Fire') & (df['HP']>40)])
new_df=(df.loc[(df['Type 1']=='Grass')  & (df['Type 2']=='Poison') & (df['HP']>70)])
#new_df=new_df.reset_index(drop=True)
new_df.reset_index(drop=True,inplace=True)
new_df.to_csv('filtered_data.csv')
print(new_df)

#print(df.loc[~df['Name'].str.contains('Mega')])