# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
#Exp 6.2: online Shopping System


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def show_cart(self):
        print("Cart Items:")
        for item in self.items:
            print(f"- {item}")

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def checkout(self):
        total = self.cart.calculate_total()
        print(f"Customer: {self.name}")
        print(f"Total Amount Payable: ${total:.2f}")
        print("Order Processed Successfully!")

def main():
    print("--- Online Shopping System ---")
    
    # Inventory
    p1 = Product(101, "Laptop", 800)
    p2 = Product(102, "Headphones", 50)
    p3 = Product(103, "Mouse", 20)

    # Customer Interaction
    c = Customer("Shreyas Shigwan")
    c.cart.add_item(p1)
    c.cart.add_item(p2)
    c.cart.add_item(p3)
    
    c.cart.show_cart()
    c.checkout()

if __name__ == "__main__":
    main()
