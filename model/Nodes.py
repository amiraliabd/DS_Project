from abc import ABC,abstractclassmethod


class Node:
    @abstractclassmethod
    def __init__(self):
        pass
    key = None
    # list of information
    about = []


class Person(Node):
    """
    key:
        person ID
    about list contains :
        first name
        last name
        birthday
        birth place
        place of work
    """
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)


class Bank(Node):
    """
    key:
        Bank account number
    about list contains :
        owner ID
        bank name
        number
    """
    def __init__(self, a: dict):
        for k in a.keys():
            self.key = k
            for value in a.get(k):
                self.about.append(value)
        pass  # from and to must be complete


class Home(Node):
    """
    key:
        postal code
    about list contains :
        owner ID
        cost
        area
        address
    """

    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete

class Car(Node):
    """
    key:
        plate number
    about list contains :
    owner ID
    model
    """
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete


class Phone(Node):
    """
    key:
        number
    about list contains :
        owner ID
        operator name
    """
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)
        pass#from and to must be complete


