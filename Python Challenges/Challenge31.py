'''You are working on a project to develop an e-commerce website. As part of the 
project, you need to implement a shopping cart functionality using OOP 
concepts in Python. Design and implement the classes for the shopping cart 
system with the following requirements: 
• The shopping cart should be able to add products, remove products, and 
calculate the total price of all the products in the cart. 
• Each product should have a name, price, and quantity. 
• The shopping cart should be able to handle multiple instances of the same 
product and update the quantity accordingly. 
• Design the classes and provide the python code implementation for the 
shopping cart system. '''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price} x {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product):
        if product.name in self.cart:
            self.cart[product.name].quantity += product.quantity
        else:
            self.cart[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]

    def calculate_total(self):
        total = 0
        for product in self.cart.values():
            total += product.price * product.quantity
        return total

    def __str__(self):
        cart_contents = "\n".join(str(product) for product in self.cart.values())
        return f"Shopping Cart:\n{cart_contents}\nTotal: {self.calculate_total()}"

# Example usage
p1 = Product("Laptop", 1000, 1)
p2 = Product("Mouse", 50, 2)
p3 = Product("Keyboard", 100, 1)

cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

print(cart)
