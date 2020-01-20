import pandas as pd
from prettytable import from_csv
from tabulate import tabulate
import networkx as nx
from itertools import combinations
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
relationDF = pd.read_csv("sample data/relationships.csv")
accountDF = pd.read_csv('sample data/accounts.csv')
callDF = pd.read_csv('sample data/calls.csv')
carDF = pd.read_csv('sample data/cars.csv')
homeDF = pd.read_csv('sample data/homes.csv')
ownershipDF = pd.read_csv('sample data/ownerships.csv')
peopleDF = pd.read_csv('sample data/people.csv')
phoneDF = pd.read_csv('sample data/phones.csv')
relationshipDF = pd.read_csv('sample data/relationships.csv')
transactionDF = pd.read_csv('sample data/transactions.csv')
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
ls=[df['from'].iloc[i] for i in range(len(df))]
#print(tabulate(df,tablefmt='psql',headers='keys'))
result0=peopleDF.loc[(peopleDF['ssn'].isin(ls)) & ((peopleDF['work']=='گمرک') | (peopleDF['work'].str.contains('بندر') ) )]
#print(tabulate(result0, tablefmt='psql', headers='keys'))
ls=[result0['ssn'].iloc[i] for i in range(len(result0))]
rel=['PARENT', 'OFFSPRING', 'SPOUSE', 'SIBLING']
result1=relationshipDF.loc[( (relationshipDF['from'].isin(ls)) |(relationshipDF['to'].isin(ls))) ]
#print(tabulate(result1,tablefmt='psql',headers='keys'))
result2=result1.loc[ (result1['relation'].isin(rel)) ]
#print(tabulate(final_result,tablefmt='psql',headers='keys'))
ls=[result2['from'].iloc[i] for i in range(len(result2))]
final_result=peopleDF.loc[ (peopleDF['ssn'].isin(ls))]
print(tabulate(final_result, tablefmt='psql', headers='keys'))
# faze 3:---------------------------------------------------------------------------------------------------------------
print('faze 3:---------------------------------------------------------------------------------------------------------------')


def bidirectional_pred_succ(G, source, target):
    # does BFS from both source and target and meets in the middle
    if target == source:
        return ({target: None}, {source: None}, source)

    Gpred = G.pred
    Gsucc = G.succ

    # predecesssor and successors in search
    pred = {source: None}
    succ = {target: None}

    # initialize fringes, start with forward
    forward_fringe = [source]
    reverse_fringe = [target]

    while forward_fringe and reverse_fringe:
        if len(forward_fringe) <= len(reverse_fringe):
            this_level = forward_fringe
            forward_fringe = []
            for v in this_level:
                for w in Gsucc[v]:
                    if w not in pred:
                        forward_fringe.append(w)
                        pred[w] = v
                    if w in succ:  # path found
                        return pred, succ, w
        else:
            this_level = reverse_fringe
            reverse_fringe = []
            for v in this_level:
                for w in Gpred[v]:
                    if w not in succ:
                        succ[w] = v
                        reverse_fringe.append(w)
                    if w in pred:  # found path
                        return pred, succ, w


def bidirectional_SP(G, source, target):
    results = bidirectional_pred_succ(G, source, target)
    pred, succ, w = results
    path = []
    while w is not None:
        path.append(w)
        w = pred[w]
    path.reverse()
    w = succ[path[-1]]
    while w is not None:
        path.append(w)
        w = succ[w]
    return len(path)



# making graph of transactions
TransactionsGraph = nx.Graph()
transaction = zip(transactionDF["from"], transactionDF["to"])
TransactionsGraph.add_edges_from(transaction)
TransactionsGraph = TransactionsGraph.to_directed()
#
doubt = final_result
smuglers = peopleDF.loc[(peopleDF['work'] == 'قاچاقچی')]
doubtssn = [doubt['ssn'].iloc[i] for i in range(len(doubt))]
smuglersssn = [smuglers['ssn'].iloc[j] for j in range(len(smuglers))]
doubledoubt = []
smuglersaccount = accountDF.loc[ (accountDF['ssn'].isin(smuglersssn))]
doubtsaccount = accountDF.loc[ (accountDF['ssn'].isin(doubtssn))]
fromsmugle = smuglersaccount["account_id"]
todoubt = doubtsaccount["account_id"]
for sid in fromsmugle:
    for did in todoubt:
        if TransactionsGraph.has_node(sid) and TransactionsGraph.has_node(did):
            if nx.has_path(TransactionsGraph, sid, did):
                if bidirectional_SP(TransactionsGraph, sid, did) <= 5:
                    doubledoubt.append(did)
doubt_frame=accountDF[accountDF['account_id'].isin(doubledoubt)]
ls=[doubt_frame['ssn'].iloc[i] for i in range(len(doubt_frame))]
doubt_frame=peopleDF[ peopleDF['ssn'].isin(ls) ]
print(tabulate(doubt_frame, tablefmt='psql', headers='keys'))
# faze 4:---------------------------------------------------------------------------------------------------------------
print('faze 4:---------------------------------------------------------------------------------------------------------------')
doubtssn=[doubt_frame['ssn'].iloc[i] for i in range(len(doubt_frame))]
doubtphonenumber=phoneDF[(phoneDF['ssn'].isin(doubtssn))]
lst_doubtphonenumber=[doubtphonenumber['number'].iloc[j] for j in range(len(doubtphonenumber))]
smuglerssn=[smuglers['ssn'].iloc[i] for i in range(len(smuglers))]
smuglerphonenumber=phoneDF[(phoneDF['ssn'].isin(smuglerssn))]
list_smuglerphonenumber=[smuglerphonenumber['number'].iloc[i] for i in range(len(smuglerphonenumber))]
number_result=callDF[( (callDF['from'].isin(list_smuglerphonenumber)) & (callDF['to'].isin(lst_doubtphonenumber)) )]
final_list=[number_result['to'].iloc[i] for i in range(len(number_result))]
final_Frame=phoneDF[ (phoneDF['number'].isin(final_list)) ]
final_list=[final_Frame['ssn'].iloc[i] for i in range(len(final_Frame))]
final_Frame=peopleDF[ (peopleDF['ssn'].isin(final_list)) ]
print(tabulate(final_Frame, tablefmt='psql', headers='keys'))

