import pandas as pd
from prettytable import from_csv
from tabulate import tabulate
from Reader import Readcsv as rc
df=rc.ownershipDF.loc[(rc.ownershipDF['date']>='2018-00-00') & (rc.ownershipDF['date']<='2020-00-00')]
ls=[]
for i in range(len(df)):
    ls.append(df['from'].iloc[i])
#print(tabulate(df,tablefmt='psql',headers='keys'))
result0=rc.peopleDF.loc[(rc.peopleDF['ssn'].isin(ls)) & ((rc.peopleDF['work']=='گمرک') | (rc.peopleDF['work'].str.contains('بندر') ) )]
#print(tabulate(result0,tablefmt='psql',headers='keys'))
ls=[]
for i in range(len(result0)):
    ls.append(result0['ssn'].iloc[i])
rel=['PARENT','OFFSPRING','SPOUSE','SIBLING']
result1=rc.relationshipDF.loc[( (rc.relationshipDF['from'].isin(ls)) |(rc.relationshipDF['to'].isin(ls))) ]
#print(tabulate(result1,tablefmt='psql',headers='keys'))
result2=result1.loc[ (result1['relation'].isin(rel)) ]
#print(tabulate(final_result,tablefmt='psql',headers='keys'))
ls=[]
for i in range(len(result2)):
    ls.append(result2['from'].iloc[i])
final_result=rc.peopleDF.loc[ (rc.peopleDF['ssn'].isin(ls))]
print(tabulate(final_result,tablefmt='psql',headers='keys'))