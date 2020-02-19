# DS_Project
this is data structure project for University
in this project we have 5 csv_files include people,bank account,home,car,phone number; as our NODE
and ownership, transaction, call, relation; as EDGE
each file has a column as unique value and these values are foreign key in other files
the story:::
police detect smugglers and they are trying to find people who are smugler's connection in 
money-laundering.
phase 1:
police ask you to read and show the data of csv files in tables
phase 2:
police think the connections must buy car or home for themselves or for Their first order family in last 2 years. you must find theme
phase 3:
to be sure that people founded in faze 2 to be criminal police ask you to check if money is transferd to their bank account by max 5 transactions.
filter people in faze 2 and show them again
phase 4:
to be certain police asks you to fined pople in faze 4 who has phone call from smuglers.
............................................................................................
about implementation:
first we try to use object oriented programmin(OOP):
we create a abstract class (NODE and edge) and try to connect them together by list of pointers in each object of thier subclasses(a node has list of the adge comes in or goes out and edges has attributes 'from' and 'to' wich defines the nodes)
but after implementing we found out this strategy is too slow.
so we chang strategy in >>change strategy commit<<
we try to use query in PANDAS 
((except faze 3 because TA insist on implementing graph,BFS,DFS and things like this))






