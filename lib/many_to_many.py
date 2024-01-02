class Author:
    all = []
    def __init__(self,name):
        self.name = name
        Author.all.append(self)
    def contracts(self):
        clist = []
        for contract in Contract.all:
            if contract.author is self:
                clist.append(contract)
        return clist
    
    def books(self):
        blist = []
        for contract in Contract.all:
            if contract.author is self and contract.book not in blist:
                blist.append(contract.book)
        return blist
    
    def sign_contract(self, book, date, royalties):
        return Contract(self,book,date,royalties)

    def total_royalties(self):
        sum = 0
        my_contracts = self.contracts()
        for contract in my_contracts:
            sum += contract.royalties
        return sum


class Book:
    all = []
    def __init__(self,title):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        clist = []
        for contract in Contract.all:
            if contract.book is self:
                clist.append(contract)
        return clist
    def authors(self):
        alist = []
        for contract in Contract.all:
            if contract.book is self and contract.author not in alist:
                alist.append(contract.author)
        return alist


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author
    def set_author(self,value):
        if type(value) is Author:
            self._author = value
        else:
            raise Exception("NOT VALID DATA")
    author = property(get_author,set_author)

    def get_book(self):
        return self._book
    def set_book(self,value):
        if type(value) is Book:
            self._book = value
        else:
            raise Exception("NOT VALID DATA")
    book = property(get_book,set_book)

    def get_date(self):
        return self._date
    def set_date(self,value):
        if type(value) is str:
            self._date = value
        else:
            raise Exception("NOT VALID DATA")
    date = property(get_date,set_date)

    def get_royalties(self):
        return self._royalties
    def set_royalties(self,value):
        if type(value) is int:
            self._royalties = value
        else:
            raise Exception("NOT VALID DATA")
    royalties = property(get_royalties,set_royalties)

    @classmethod
    def contracts_by_date(cls,date):
        clist = []
        for contract in cls.all:
            if contract.date == date:
                clist.append(contract)
        return clist
