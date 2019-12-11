from abc import ABC,abstractclassmethod
class Node:
    @abstractclassmethod
    def __init__(self):
        pass
    #edge witch is comming in or going out
    IN=[]
    OUT=[]
    key = None
    # list of information
    about = []

