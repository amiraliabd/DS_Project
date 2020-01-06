
import pandas as pd

# function for making dictionary of vertexes
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

accountsdic = Reader("/home/ehsan/DS_Project/sample data/accounts.csv", 2, 4)
phonesdic = Reader("/home/ehsan/DS_Project/sample data/phones.csv", 1, 3)
peopledic = Reader("/home/ehsan/DS_Project/sample data/people.csv", 2, 6)
homesdic = Reader("/home/ehsan/DS_Project/sample data/homes.csv", 2, 5)
carsdic = Reader("/home/ehsan/DS_Project/sample data/cars.csv", 0, 4)