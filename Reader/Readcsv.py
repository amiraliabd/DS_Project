import pandas as pd
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
if accountDF== None:
    accountDF=read_account_csv()
    callDF=read_call_csv()
    carDF=read_car_csv()
    homeDF=read_home_csv()
    ownershipDF=read_ownership_csv()
    peopleDF=read_people_csv()
    phoneDF=read_phone_csv()
    relationshipDF=read_relationship_csv()
    transactionDF=read_transaction_csv()