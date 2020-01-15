import pandas as pd
from prettytable import from_csv
from tabulate import tabulate
'''
using pandas lib for making dataframes for nodes and edges

'''
accountDF=None
callDF=None
carDF=None
homeDF=None
ownershipDF=None
peopleDF=None
phoneDF=None
relationshipDF=None
transactionDF=None
def read_relation_csv():
    relationDF = pd.read_csv("sample data/relationships.csv")
    return relationDF
def read_account_csv():
    accountDF = pd.read_csv('sample data/accounts.csv')
    return accountDF
def read_call_csv():
    callDF = pd.read_csv('sample data/calls.csv')
    return callDF
def read_car_csv():
    carDF = pd.read_csv('sample data/cars.csv')
    return carDF
def read_home_csv():
    homeDF = pd.read_csv('sample data/homes.csv')
    return homeDF
def read_ownership_csv():
    ownershipDF = pd.read_csv('sample data/ownerships.csv')
    return ownershipDF
def read_people_csv():
    peopleDF = pd.read_csv('sample data/people.csv')
    return peopleDF
def read_phone_csv():
    phoneDF = pd.read_csv('sample data/phones.csv')
    return phoneDF
def read_relationship_csv():
    relationshipDF = pd.read_csv('sample data/relationships.csv')
    return relationshipDF
def read_transaction_csv():
    transactionDF = pd.read_csv('sample data/transactions.csv')
    return transactionDF

#to create this object just one time
if accountDF == None:
    accountDF=read_account_csv()
    callDF=read_call_csv()
    carDF=read_car_csv()
    homeDF=read_home_csv()
    ownershipDF=read_ownership_csv()
    peopleDF=read_people_csv()
    phoneDF=read_phone_csv()
    relationshipDF=read_relationship_csv()
    transactionDF=read_transaction_csv()

# faze 1:---------------------------------------------------------------------------------------------------------------
def Tables(address):
    filepath = open(address, "r")
    table = from_csv(filepath)
    filepath.close()
    return table
print('faze 1:---------------------------------------------------------------------------------------------------------------')
print("accounts table:")
print(Tables("sample data/accounts.csv"))
print("phones table:")
print(Tables("sample data/phones.csv"))
print("people table:")
print(Tables("sample data/people.csv"))
print("homes table:")
print(Tables("sample data/homes.csv"))
print("cars table:")
print(Tables("sample data/cars.csv"))
# faze 2:---------------------------------------------------------------------------------------------------------------
print('faze 2:---------------------------------------------------------------------------------------------------------------')
df=ownershipDF.loc[(ownershipDF['date']>='2018-00-00') & (ownershipDF['date']<='2020-00-00')]
ls=[]
for i in range(len(df)):
    ls.append(df['from'].iloc[i])
#print(tabulate(df,tablefmt='psql',headers='keys'))
result0=peopleDF.loc[(peopleDF['ssn'].isin(ls)) & ((peopleDF['work']=='گمرک') | (peopleDF['work'].str.contains('بندر') ) )]
#print(tabulate(result0, tablefmt='psql', headers='keys'))
ls=[]
for i in range(len(result0)):
    ls.append(result0['ssn'].iloc[i])
rel=['PARENT', 'OFFSPRING', 'SPOUSE', 'SIBLING']
result1=relationshipDF.loc[( (relationshipDF['from'].isin(ls)) |(relationshipDF['to'].isin(ls))) ]
#print(tabulate(result1,tablefmt='psql',headers='keys'))
result2=result1.loc[ (result1['relation'].isin(rel)) ]
#print(tabulate(final_result,tablefmt='psql',headers='keys'))
ls=[]
for i in range(len(result2)):
    ls.append(result2['from'].iloc[i])
final_result=peopleDF.loc[ (peopleDF['ssn'].isin(ls))]
print(tabulate(final_result, tablefmt='psql', headers='keys'))
# faze 3:---------------------------------------------------------------------------------------------------------------
print('faze 3:---------------------------------------------------------------------------------------------------------------')

# faze 4:---------------------------------------------------------------------------------------------------------------
print('faze 4:---------------------------------------------------------------------------------------------------------------')