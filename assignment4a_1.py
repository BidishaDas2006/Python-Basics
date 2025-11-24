#Q.1
class BankAccount:
    def __init__(self,balance,acc_no,owner_name):
        self.balance=balance
        self.acc_no=acc_no
        self.owner_name=owner_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"Rs. -> {amount} is deposited.")

    def withdrawl(self,amount):
        self.balance-=amount
        print(f"Rs. -> {amount} is debited .")

    def check_balance(self):
        return self.balance
    

acc1=BankAccount(10000,123241203036,"Bidisha")
print(acc1.balance)  

acc2=BankAccount(12000,123241203037,"bob")
print(acc2.balance)

acc1.deposit(4000)
acc1.withdrawl(6000)
print(acc1.check_balance())


#Q.2

class book:
    def __init__(self,title,author,reviews):
        self.title=title
        self.author=author
        self.reviews=reviews

    def new_review(self,new_review):
        self.reviews.append(new_review)
        print(f"{new_review} is added.")

    def count_review(self):
        count=len(self.reviews)
        print(f"total reviews given:{count}") 
        return count   

              


    def display_review(self):
        for review in self.reviews:
            print(review)

            
book1=book("magic","harry",["good","brilliant"])

book1.new_review("fantastic")
print(book1.count_review())
book1.display_review()

#Q.3

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    def get_name(self):
        return self.__name  

    def set_name(self,name):
        cleaned = name.strip()
        if cleaned == "":
            raise ValueError("Name cannot be empty.")
    # save cleaned name
        self.__name = cleaned

    def get_roll_number(self):
        return self.__roll_no
    def set_roll_number(self,roll_no):
        if   (1<=self.__roll_no<=100 ):
            raise ValueError("Roll number must be between 1 and 100.")
        self.__roll_no=roll_no

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if (marks<0) :
            raise ValueError("Marks cannot be negative.")
        self.__marks=marks
        

s = Student("bidisha", 12, -5)




print(s.get_name())  
print(s.get_marks())
s2=Student("", 5, 70)
s2.set_name("")









            
    

    

