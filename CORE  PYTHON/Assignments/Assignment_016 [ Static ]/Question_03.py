
# Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.




class Shirt:
    base_price = 1000

    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        size_price = self.get_price()
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", size_price)

    def get_price(self):
        size = self.size.lower()

        if size == "small":
            return Shirt.base_price
        elif size == "medium":
            return Shirt.base_price * 1.10
        elif size == "large":
            return Shirt.base_price * 1.20
        elif size == "xlarge":
            return Shirt.base_price * 1.30
        else:
            return Shirt.base_price

    def __del__(self):
        print("Shirt object destroyed")


s1 = Shirt(101, "Formal Shirt", "Formal", Shirt.base_price, "Small")
s2 = Shirt(102, "Formal Shirt", "Formal", Shirt.base_price, "Medium")
s3 = Shirt(103, "Formal Shirt", "Formal", Shirt.base_price, "Large")
s4 = Shirt(104, "Formal Shirt", "Formal", Shirt.base_price, "XLarge")

s1.ShowBook()
print()
s2.ShowBook()
print()
s3.ShowBook()
print()
s4.ShowBook()