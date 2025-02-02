# Class and Object
# 1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
from tabulate import tabulate
class Employee:
    emp_list = {}
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept
        Employee.emp_list[id] = {name, dept}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Enter name: ")
    id = input("Enter id: ")
    dept = input("Enter department: ")
    e = Employee(name, id, dept)
print(tabulate(Employee.emp_list, headers=["ID", "Name", "Department"], tablefmt="grid"))

# 2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
class BankAccount:
    total_balance = 0
    def deposit(self, amount):
        self.amount = amount
        BankAccount.total_balance += amount
    def withdraw(self, amount):
        self.amount = amount
        BankAccount.total_balance -= amount

bank = BankAccount()
n = int(input("Enter number of operations: "))
for i in range(n):
    choice = int(input("\n1. Press 1 for deposit\n2. Press 2 for withdrawal\n3. Press 3 for total balance\nEnter your choice: "))
    match choice:
        case 1:
            depositAmt = int(input("Enter amount to deposit: "))
            bank.deposit(depositAmt)
        case 2:
            withdrawAmt = int(input("Enter amount to withdraw: "))
            if BankAccount.total_balance >= withdrawAmt:
                bank.withdraw(withdrawAmt)
        case 3:
            print(BankAccount.total_balance)

# 3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
class Book:
    booksList = {}
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.booksList[isbn] = {title, author}
    @classmethod
    def displayBookDetails(self):
        for val in Book.booksList.items():
            print(val)
        # print(tabulate(Book.booksList, headers=["ISBN", "Title", "Author"], tablefmt="grid"))
n = int(input("Enter number of books: "))
for i in range(n):
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    book = Book(title, author, isbn)

Book.displayBookDetails()

# 4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def studentDetails(self):
        print(f"Student Name: {self.name}\nStudent Roll No: {self.roll_number}")

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    stu = Student(name, roll)
    stu.studentDetails()

# 5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def check_availability(self, quantity):
        self.quantity = quantity
        if self.stock >= quantity:
            print(f"Requested quantity of {self.quantity} is available")
        else:
            print("Stock is not available!")
n = int(input("Enter no of products: "))
for i in range(n):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    prod = Product(name, price, stock)
    quantity = int(input("Enter quantity: "))
    prod.check_availability(quantity)