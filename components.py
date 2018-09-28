# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []
    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for product in self.products:
            print (product)
        print ("Enter back to go to the main menu, or checkout to exit.")

class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        # your code goes here!
        return str("\nProduct Name: %s\nProduct Description: %s\nPrice: %s KD\n" %(self.name, self.description, self.price))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products =[]

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for product in self.products:
            total = total + product.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print ("")
        print ("------------------------------------------------------------------------")
        print ("Your cart includes the following:")
        for product in self.products:
            print ("\t  %s" %product)
        print ("Your total is: %s KD" %self.get_total_price())
        print ("------------------------------------------------------------------------")
    
    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        ans = input ("Confirm your order? (Y/N)?  ")
        if ans == "Y" or ans == "y": #if ans.lower() == "y"
            print ("\nYour order has been placed!")
        elif ans == "N" or ans == "n":
            print ("\nYour order has been cancelled.\nSee you soon!")