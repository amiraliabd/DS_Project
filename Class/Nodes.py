class Node:
    def __init__(self,key,ls:[]):
        self.key = None
    # list of information
        self.about = []
    # list for Edge
        self.OUT=[]
        self.IN=[]
        self.key=key
        for value in ls:
            self.about.append(value)

            
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


class Bank(Node):
    """
    key:
        Bank account number
    about list contains :
        owner ID
        bank name
        number
    """


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


class Car(Node):
    """
    key:
        plate number
    about list contains :
    owner ID
    model
    color
    """


class Phone(Node):
    """
    key:
        number
    about list contains :
        owner ID
        operator name
    """