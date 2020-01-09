
import pandas as pd
# function for making dictionary of vertexes and edges
def Reader(address, middle, end):
    csv = pd.read_csv(address)
    csv.head()
    infodic = {}
    if middle == 0:
        for k in range(len(csv)):
            infodic[csv.iloc[k][0]] = []
            for v in range(1, end):
                infodic[csv.iloc[k][0]].append(csv.iloc[k][v])
    else:
        for k in range(len(csv)):
            infodic[csv.iloc[k][middle]] = []
            for v in range(0, middle):
                infodic[csv.iloc[k][middle]].append(csv.iloc[k][v])
            for v in range(middle + 1, end):
                infodic[csv.iloc[k][middle]].append(csv.iloc[k][v])
    return infodic
# making relationship dictionary
relationcsv = pd.read_csv("sample data/relationships.csv")
relationshipsdic = {}
for i in range(len(relationcsv)):
    key = str(relationcsv.iloc[i][0]) + str(relationcsv.iloc[i][1])
    relationshipsdic[key] = []
    for j in range(2, 4):
        relationshipsdic[key].append(relationcsv.iloc[i][j])
# Calling Reader function for making vertexes dictionary
accountsdic = Reader("sample data/accounts.csv", 2, 4)
phonesdic = Reader("sample data/phones.csv", 1, 3)
peopledic = Reader("sample data/people.csv", 2, 6)
homesdic = Reader("sample data/homes.csv", 2, 5)
carsdic = Reader("sample data/cars.csv", 0, 4)
# Calling Reader function for making edges dictionary
ownershipsdic = Reader("sample data/ownerships.csv", 2, 5)
transactionsdic = Reader("sample data/transactions.csv", 2, 5)
callsdic = Reader("sample data/calls.csv", 2, 5)

