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

class Person(Node):
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete


class banck(Node):
    def __init__(self, a: dict):
        for k in a.keys():
            self.key = k
            for value in a.get(k):
                self.about.append(value)
        pass  # from and to must be complete

class home(Node):
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete

class car(Node):
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete

class phone(Node):
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete


