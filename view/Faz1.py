
import pandas as pd
from prettytable import from_csv
def Tables(address):
    filepath = open(address, "r")
    table = from_csv(filepath)
    filepath.close()
    return table

print("accounts table:")    
print(Tables("/home/ehsan/DS_Project/sample data/accounts.csv"))
print("phones table:")
print(Tables("/home/ehsan/DS_Project/sample data/phones.csv"))
print("people table:")
print(Tables("/home/ehsan/DS_Project/sample data/people.csv"))
print("homes table:")
print(Tables("/home/ehsan/DS_Project/sample data/homes.csv"))
print("cars table:")
print(Tables("/home/ehsan/DS_Project/sample data/cars.csv"))