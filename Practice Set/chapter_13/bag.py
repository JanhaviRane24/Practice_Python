class Bag:
    def __init__(self,book,pen):

        self.book=book
        self._pen=pen
        self.__notes="science test important"

    def add_item(self,book,pen):
        self.book=self.book+book
        print(" no of booked added",book)
        self._pen=self._pen+pen
        print(" no of pen added",pen)


    def remove_item(self,book,pen):
        self.book=self.book-book
        print("no of booked removed",book)

        self._pen=self._pen-pen
        print("no of pen removed",self._pen)

    def display(self):
        print("no of books",self.book)
        print("no of pen",self._pen)
        print("notes",self.__notes)

b=Bag(3,2)
# b.display()
# b.add_item(1,4)
# b.display()
# b.remove_item(2,1)
# b.display()
print(b.book)          # Public
print(b._pen)          # Protected
# print(b.__notes)
#AttributeError: 'Bag' object has no attribute '__notes'
print(b._Bag__notes)# Private using name mangling

# Why Name Mangling?

# Python uses name mangling to reduce the chance of accidentally overriding private attributes in subclasses. It is not meant as strict security.