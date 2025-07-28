'''You are developing a system to handle different payment methods. Implement an 
abstract class called PaymentMethod with an abstract method processPayment(). 
The processPayment() 
method should be implemented by the concrete classes 
that inherit from PaymentMethod and should simulate the payment processing 
for each specific payment method. 
Create two concrete classes CreditCardPayment 
and PayPalPayment 
extend the PaymentMethod class. Implement the processPayment() 
that 
method in 
both classes to display a message indicating the payment method being 
processed. 
Write the abstract class PaymentMethod , the concrete classes CreditCardPayment 
and PayPalPayment , and the code to demonstrate polymorphism.'''
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def processPayment(self, amount):
        print(f"Processing credit card payment of ${amount}.")

class PayPalPayment(PaymentMethod):
    def processPayment(self, amount):
        print(f"Processing PayPal payment of ${amount}.")

if __name__ == "__main__":
    methods = [CreditCardPayment(), PayPalPayment()]
    for method in methods:
        method.processPayment(10)