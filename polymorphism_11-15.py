# Polymorphism
# 11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self, error=None, warning=None, info=None):
        self.error = error
        self.warning = warning
        self.info = info
        if error and warning and info:
            print(f"Error message: {error}\nWarning message: {warning}!\nInformation message: {info}")
        elif error and warning:
            print(f"Error message: {error}\nWarning message: {warning}!")
        elif error and info:
            print(f"Error message: {error}\nInformation message: {info}")
        elif error:
            print(f"Error message: {error}")
        elif warning and info:
            print(f"Warning message: {warning}!\nInformation message: {info}")
        elif warning:
            print(f"Warning message: {warning}!")
        else:
            print(f"Information message: {error}")
obj = Logger()
obj.log(error="Keyword error")
obj.log(error="Keyword error", warning="Warning msg")
obj.log(error="Keyword error", warning="First warning", info="Use correct keyword")
obj.log(warning="Second warning")
obj.log(warning="Second warning", info="Second info")

# 12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def process_payment(self):
        print("Process payment is still pending...")
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using credit card")
class PayPalPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using PayPal")
class BitcoinPayment(Payment):
    def process_payment(self):
        print("Payment is achieved using Bitcoin")
creditcard = CreditCardPayment()
creditcard.process_payment()
paypal = PayPalPayment()
paypal.process_payment()
bitcoin = BitcoinPayment()
bitcoin.process_payment()

# 13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        print("No information to find the area")
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print(f"Area of square is: {self.side*self.side}")
class Triangle(Shape):
    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height
    def area(self):
        print(f"Area of triangle is: {0.5*self.breadth*self.height}")
square = Square(4)
square.area()
triangle = Triangle(4, 4)
triangle.area()

# 14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        print("Sent notification from Notification class")
class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS notification send")
email = EmailNotification()
email.send()
sms = SMSNotification()
sms.send()

# 15. Write an example where `Operator Overloading` is used to concatenate two `Book` objects, treating them as a series.
# Operator Overloading