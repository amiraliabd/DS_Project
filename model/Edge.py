from abc import ABC,abstractclassmethod


class Edge:
    @abstractclassmethod
    def __init__(self):
    #FROM witch  TO witch one
        self.FROM=None
        self.TO=None
    #list of information
        self.about=[]


class OwnerShip(Edge):
    """
    key:
        Registration Document Number
    about list contains :
        from whom
        to what
        date of own
        payment
    """
    def __init__(self, a:dict):
        for k in a.keys():
            self.key=k
            for value in a.get(k):
                self.about.append(value)


class Transactions(Edge):
    """
        key:
            number of transaction
        about list contains :
            from where
            to where
            date of transaction
            payment
        """

    def __init__(self, a: dict):
        for k in a.keys():
            self.key = k
            for value in a.get(k):
                self.about.append(value)


class Call(Edge):
    """
    key:
        number of call
    about list contains :
        from a number
        to a number
        call number
        date of call
        how long does calling takes
           """

    def __init__(self, a: dict):
        for k in a.keys():
            self.key = k
            for value in a.get(k):
                self.about.append(value)


class Relation(Edge):
    """
    key:
        combine of persons ID
    about list contains :
        from who
        to who
        relation
        when relation starts
           """
    def __init__(self, a: dict):
        for k in a.keys():
            self.key = k
            for value in a.get(k):
                self.about.append(value)