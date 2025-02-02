# Interface -> Using Abstract Base Classes - ABC
from abc import ABC, abstractmethod
# 16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
class IShape:
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        print(f"Area of rectangle is: {self.length*self.breadth}")
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        print(f"Area of circle is: {3.14*self.radius*self.radius}")
rect = Rectangle(15,6)
rect.calculate_area()
cir = Circle(2)
cir.calculate_area()

# 17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
class IDatabaseOperations:
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data in SQL database")
    def update(self):
        print("Updating data in SQL database")
    def delete(self):
        print("Deleting data in SQL database")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data in NoSQL database")
    def update(self):
        print("Updating data in NoSQL database")
    def delete(self):
        print("Deleting data in NoSQL database")
sql = SQLDatabase()
sql.insert()
sql.delete()
nosql = NoSQLDatabase()
nosql.insert()
nosql.delete()

# 18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
class ICalculator:
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
class Calculator(ICalculator):
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Addition: {num1+num2}")
    def subtract(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Subtraction: {num1-num2}")
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Multiplication: {num1*num2}")
    def divide(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Division: {num1/num2}")

calc = Calculator()
calc.add(10, 5)
calc.subtract(50, 15)
calc.multiply(15, 6)
calc.divide(100, 20)

# 19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
class IVehicle:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine started")
    def stop_engine(self):
        print("Bike engine stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine started")
    def stop_engine(self):
        print("Truck engine stopped")
car = Car()
car.start_engine()
car.stop_engine()
bike = Bike()
bike.start_engine()
bike.stop_engine()
truck = Truck()
truck.start_engine()
truck.stop_engine()

# 20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
class UserAuthentication:
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in using Google")
    def logout(self):
        print("Logged out of Google account")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in using Facebook account")
    def logout(self):
        print("Logged out of Facebook account")
google = GoogleAuth()
google.login()
google.logout()
facebook = FacebookAuth()
facebook.login()
facebook.logout()