from Reader import Readcsv
from Class import Edge
from Class import Nodes
Readcsv.execute()
person_nodelist=[]
account_nodelist=[]
home_nodelist=[]
car_nodelist=[]
ownership_edgelist=[]
transaction_edgelist=[]
call_edgelist=[]
relation_edgelist=[]
for key in sorted(Readcsv.peopledic):
    person_nodelist.append(Nodes.Person(key,Readcsv.peopledic.get(key)))
for key in sorted(Readcsv.accountsdic):
    account_nodelist.append(Nodes.Bank(key,Readcsv.accountsdic.get(key)))
for key in sorted(Readcsv.homesdic):
    home_nodelist.append(Nodes.Home(key,Readcsv.homesdic.get(key)))
for key in sorted(Readcsv.carsdic):
    car_nodelist.append(Nodes.Car(key,Readcsv.carsdic.get(key)))
#__________________-_________________
def BS(lys, val):

    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid.key] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return lys[index]


for key in Readcsv.ownershipsdic:
    #adding edge to list of edges
    ownership_edgelist.append(Edge.OwnerShip(key,Readcsv.ownershipsdic.get(key)))
    #adding Node pointer in edge attribute(FROM)
    ownership_edgelist[-1].FROM=BS(person_nodelist,ownership_edgelist[-1].about[0])
    #adding Edge pointer to Node attribute(OUT)
    ownership_edgelist[-1].FROM.OUT.apppend(ownership_edgelist[-1])
    if ownership_edgelist[-1].about[1].isdigit():
        ownership_edgelist[-1].TO = BS(home_nodelist, ownership_edgelist[-1].about[1])
    else:
        for car in car_nodelist:
            if car.key==ownership_edgelist[-1].about[1]:
                ownership_edgelist[-1].TO=car
for key in Readcsv.transactionsdic:
    transaction_edgelist.append(Edge.Transactions(key,Readcsv.transactionsdic.grt(key)))
for key in Readcsv.callsdic:
    call_edgelist.append(Edge.Call(key,Readcsv.callsdic.get(key)))
#no relation in Readcsv.py