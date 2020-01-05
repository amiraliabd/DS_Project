class Edge:
    def __init__(self, key, ls:[]):
    #FROM witch  TO witch one
        self.FROM=None
        self.TO=None
    #list of information
        self.about=[]
        self.key=None
        self.key = key
        for value in ls:
            self.about.append(value)


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