from Book import *

def add_book():
    ch = "Y"
    while(ch == "Y" or ch == "YES"):
        with open("Books.txt","a") as f:
            b_rno = int(input("Enter Book Register Number :"))
            b_name = input("Enter Book Name :")
            b_details = input("Enter Book Details :")
            b_auther = input("Enter Book Auther Name :")
            b_price = int(input("Enter Book Price :"))
            f.write(str(b_rno)+"\n")
            f.write(b_name+"\n")
            f.write(b_details+"\n")
            f.write(b_auther+"\n")
            f.write(str(b_price)+"\n")
        print("Added New Book in record Successfully..")
        ch = input("Do you want to add another Book in record ? (YES/NO) ")

def show_book():
    print("======================== Books Record ========================")
    with open("Books.txt") as f:
        for line in f:
            b_rno = line.strip()
            b_name = f.readline().strip()
            b_details = f.readline().strip()
            b_auther = f.readline().strip()
            b_price = f.readline().strip()
            b=Book(b_rno,b_name,b_details,b_auther,b_price)
            print(b)

def search_book():
    s_name=input("Enter book name to Search:")
    F=False
    with open("Books.txt") as f:
        for line in f:
            b_rno = line.strip()
            b_name = f.readline().strip()
            b_details = f.readline().strip()
            b_auther = f.readline().strip()
            b_price = f.readline().strip()
            b=Book(b_rno,b_name,b_details,b_auther,b_price)
            if (b.book_name == s_name):
                print("Book Details")
                print(b)
                F=True
                break
    if F==False:
        print("Book doesn't exist in the record..")

def update_book():
    s_name=input("Enter book name to Update details:")
    F=False
    li=[]
    with open("Books.txt") as f:
        for line in f:
            b_rno = line.strip()
            b_name = f.readline().strip()
            b_details = f.readline().strip()
            b_auther = f.readline().strip()
            b_price = f.readline().strip()
            b=Book(b_rno,b_name,b_details,b_auther,b_price)
            if (b.book_name == s_name):
                print("Book Details")
                print(b)
                F=True
                ch = int(input("Enter the field to update :\n1.Book register num\n2.Book name\n3.Book Details\n4.Book auther name\n5.Book Price\n"))
                if (ch == 1):
                    b.book_rno = input("Enter modified Book Register num :")
                elif (ch == 2):
                    b.book_name = input("Enter modified Book name :")
                elif (ch == 3):
                    b.book_details = input("Enter modified Book details :")
                elif (ch == 4):
                    b.book_auther = input("Enter modified Book auther name :")
                elif (ch == 5):
                    b.book_price = input("Enter modified Book price :")
            li.append(b)
    if F==False:
        print("Book doesn't exist in the record..")
    with open("Books.txt","w") as f:
        for bk in li:
            f.write(str(bk.book_rno)+"\n")
            f.write(bk.book_name+"\n")
            f.write(bk.book_details+"\n")
            f.write(bk.book_auther+"\n")
            f.write(str(bk.book_price)+"\n")
        print("Details Updated Successfully..")

def delete_book():
    s_name=input("Enter book name to delete:")
    F=False
    li=[]
    with open("Books.txt") as f:
        for line in f:
            b_rno = line.strip()
            b_name = f.readline().strip()
            b_details = f.readline().strip()
            b_auther = f.readline().strip()
            b_price = f.readline().strip()
            b=Book(b_rno,b_name,b_details,b_auther,b_price)
            if (b.book_name == s_name):
                print("Book Details")
                print(b)
                F=True
            else:
                li.append(b)
    if F==False:
        print("Book doesn't exist in the record..")
    with open("Books.txt","w") as f:
        for bk in li:
            f.write(str(bk.book_rno)+"\n")
            f.write(bk.book_name+"\n")
            f.write(bk.book_details+"\n")
            f.write(bk.book_auther+"\n")
            f.write(str(bk.book_price)+"\n")
        print("Book deleted from record Successfully..")


def Purchase_Book():
    ch = "Y"
    while(ch == "Y" or ch == "YES"):
        s_name=input("Enter book name which want you to buy:")
        F=False
        with open("Books.txt") as f:
            for line in f:
                b_rno = line.strip()
                b_name = f.readline().strip()
                b_details = f.readline().strip()
                b_auther = f.readline().strip()
                b_price = f.readline().strip()
                b=Book(b_rno,b_name,b_details,b_auther,b_price)
                if (b.book_name == s_name):
                    print("Book Details")
                    print(b)
                    with open("order.txt","a") as fi:
                        fi.write(str(b_rno)+"\n")
                        fi.write(b_name+"\n")
                        fi.write(b_details+"\n")
                        fi.write(b_auther+"\n")
                        fi.write(str(b_price)+"\n")
                    F=True
                    break
        if F==False:
            print("Book doesn't exist in the record..")
        ch = input("Do you want to add another Book to buy ? (YES/NO) ")
    ch1 = input("Print Bill Recipt ? (P) ")
    if (ch1 == "P"):
            print(("*")*25);
            print("Bill Recipt")
            print(("*")*25);
            x=[]
            sum=0
            with open("order.txt") as fa:
                for line in fa:
                    b_rno = line.strip()
                    b_name = fa.readline().strip()
                    b_details = fa.readline().strip()
                    b_auther = fa.readline().strip()
                    b_price = fa.readline().strip()
                    b=Book(b_rno,b_name,b_details,b_auther,b_price)
                    print(b)
                    x.append(b.book_price)
            for s in range(0,len(x)):
                sum=sum+int(x[s])
    print("*"*25)
    print ("Total bill amount : ",sum,"Rs")   


def ad_menu():
    ch = "Y"
    while(ch == "Y" or ch == "YES"):
        c = int(input("Enter your choice :\n1.Add Book\n2.Show all books Record\n3.Search books\n4.Update book details\n5.Delete book\n"))
        if (c == 1):
            add_book()
        elif (c == 2):
            show_book()
        elif (c == 3):
            search_book()
        elif (c == 4):
            update_book()
        elif (c == 5):
            delete_book()
        ch = input("Do you want to continue to the main menu ? (YES/NO) ")




def u_menu():
    ch = "Y"
    while(ch == "Y" or ch == "YES"):
        c = int(input("Enter your choice :\n1.Show all books Record\n2.Search books\n3.Purchase Book\n"))
        if (c == 1):
            show_book()
        elif (c == 2):
            search_book()
        elif (c == 3):
            Purchase_Book()

        ch = input("Do you want to continue to the main menu ? (YES/NO) ")

