class Book:
    def __init__(self,b_rno,b_name,b_details,b_auther,b_price):
        self.book_rno=b_rno
        self.book_name=b_name
        self.book_details=b_details
        self.book_auther=b_auther
        self.book_price=b_price
    def __str__(self):
        return str(self.book_rno)+"\t"+self.book_name+"\t"+self.book_details+"\t"+self.book_auther+"\t"+str(self.book_price)

