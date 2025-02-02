# Inheritance -> Multi-level & Multiple
# 6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    name = 'Vehicle'
    def show(self):
        print("This is vehicle class method")
    def displayName(self):
        print(f"Vehicle name is: {self.name}")
class Car(Vehicle):
    def carMethod(self):
        print("This is car class method")
    def displayName(self):
        Vehicle.name = 'Car'
        print(f"Car name is: {Vehicle.name}")
class Bike(Vehicle):
    def bikeMethod(self):
        print("This is bike class method")
    def displayName(self):
        Vehicle.name = 'Bike'
        print(f"Vehicle name is: {Vehicle.name}")
class ElectricCar(Car):
    def electricCarMethod(self):
        print("This is electric car class method")
    def displayName(self):
        Vehicle.name = 'Electric Car'
        print(f"Vehicle name is: {Vehicle.name}")
ev = ElectricCar()
ev.displayName()
ev.carMethod()
ev.electricCarMethod()

# 7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
class Person:
    occupation = 'Free guy'
    def personMethod(self):
        print(f"{Person.occupation}")
class Employee(Person):
    Person.occupation = 'Employee in ABC Company'
    def employeeMethod(self):
        print(f"Employee method with occupation: {Person.occupation}")
class Manager(Employee):
    Employee.occupation = 'Manager in ABC company'
    def managerMethod(self):
        print(f"{Employee.occupation}")
    def approve_leave(self):
        print("Leave approved!")
emp = Employee()
emp.employeeMethod()
m = Manager()
m.personMethod()
m.managerMethod()
m.approve_leave()

# 8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal:
    def sound(self):
        print("Animals make various sounds")
    def speak(self):
        print("Animal says Hi!")
class Dog(Animal):
    def sound(self):
        print("Dogs says bow bow")
    def speak(self):
        print("Dog says Hello!")
class Cat(Animal):
    def sound(self):
        print("Cat says meow")
    def speak(self):
        print("Cat says Hai!")
dog = Dog()
dog.speak()
cat = Cat()
cat.speak()

# 9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        print("Car moves on road.")
class Airplane:
    def move(self):
        print("Plane goes over clouds.")
class FlyingCar(Car, Airplane):
    def move(self):
        super().move()
        print("Flying Car can travel on road as well as air")
fc = FlyingCar()
fc.move()

# 10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    device_category = 'Electronics'
    def scope(self):
        print("All the electronic devices")
    def showCategory(self):
        print(f"Category is: {Electronics.device_category}")
class MobileDevice(Electronics):
    Electronics.device_category  = "Mobile Device"
    def scope(self):
        print("Electronic devices that are mobile phones")
class SmartPhone(MobileDevice):
    Electronics.device_category  = "Smart Phone"
    def scope(self):
        print("All the mobile phones that are smart phones")
sp = SmartPhone()
sp.scope()
sp.showCategory()