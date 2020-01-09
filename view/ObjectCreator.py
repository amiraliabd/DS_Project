from Reader import Readcsv
from Class import Edge
from Class import Nodes
#########################################################################







#no relation in Readcsv.py







########################################################################
person_nodelist=[]
account_nodelist=[]
home_nodelist=[]
car_nodelist=[]
phone_nodelist=[]
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
for key in sorted(Readcsv.phonesdic):
    phone_nodelist.append(Nodes.Phone(key,Readcsv.phonesdic.get(key)))
___________________________________

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
        ownership_edgelist[-1].TO.IN.append(ownership_edgelist[-1])
    else:
        for car in car_nodelist:
            if car.key==ownership_edgelist[-1].about[1]:
                ownership_edgelist[-1].TO=car
                car.OUT=ownership_edgelist[-1]
                break
for key in Readcsv.transactionsdic:
    transaction_edgelist.append(Edge.Transactions(key,Readcsv.transactionsdic.grt(key)))
    transaction_edgelist[-1].FROM=BS(account_nodelist,transaction_edgelist[-1].about[0])
    transaction_edgelist[-1].FROM.OUT.append(transaction_edgelist[-1])
    transaction_edgelist[-1].TO = BS(account_nodelist, transaction_edgelist[-1].about[1])
    transaction_edgelist[-1].TO.IN.append(transaction_edgelist[-1])
for key in Readcsv.callsdic:
    call_edgelist.append(Edge.Call(key,Readcsv.callsdic.get(key)))
    call_edgelist[-1].FROM=BS(phone_nodelist,call_edgelist[-1].about[0])
    call_edgelist[-1].FROM.OUT.append(call_edgelist[-1])
    call_edgelist[-1].TO=BS(phone_nodelist,call_edgelist[-1].about[1])
    call_edgelist[-1].TO.IN.append(call_edgelist[-1])
