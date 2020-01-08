
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

def execute():
    # Calling Reader function for making vertexes dictionary
    accountsdic = Reader("/home/ehsan/DS_Project/sample data/accounts.csv", 2, 4)
    phonesdic = Reader("/home/ehsan/DS_Project/sample data/phones.csv", 1, 3)
    peopledic = Reader("/home/ehsan/DS_Project/sample data/people.csv", 2, 6)
    homesdic = Reader("/home/ehsan/DS_Project/sample data/homes.csv", 2, 5)
    carsdic = Reader("/home/ehsan/DS_Project/sample data/cars.csv", 0, 4)
    # Calling Reader function for making edges dictionary
    ownershipsdic = Reader("/home/ehsan/DS_Project/sample data/ownerships.csv", 2, 5)
    transactionsdic = Reader("/home/ehsan/DS_Project/sample data/transactions.csv", 2, 5)
    callsdic = Reader("/home/ehsan/DS_Project/sample data/calls.csv", 2, 5)
    # i dont understand what should i do for relationship edge
