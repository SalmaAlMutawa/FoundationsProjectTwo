# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.shopatsalma's.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    print ("Please choose a store: ")
    for store in stores:
        print (store.name)
    print ("\nPlease choose a store name.")

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
        elif store.name.lower()=="checkout":
            return "checkout"
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    choice = input().lower()
    usr_inp = get_store(choice)
    while usr_inp == False and usr_inp != "checkout":
        choice_2 = input ("Sorry invalid store, please try again: ")
        return get_store(choice_2)
    if usr_inp == "checkout":
        return pick_products(cart, "checkout")
    return get_store(choice)
    print("\nThank you for choosing %s" %choice)
 
def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()

    user_choice = input("Choose your product: ")
    while user_choice != "back":
        if user_choice == "checkout":
            cart.checkout()
            return 
        flag = False
        for product in picked_store.products:
            # print("COMPARING %s with %s"%(user_choice.lower(), product.name.lower()))
            if user_choice.lower() == product.name.lower():
                cart.add_to_cart(product)
                flag = True
                # print("PRODUCT FOUND!")
                break
        
        if flag == False:
            print ("Sorry we don't have this product.")
        user_choice = input("\nWhat else? Or enter checkout to exit. ")

    if user_choice == "back":
        picked_store = pick_store()
        pick_products(cart, picked_store)
    



def shop():
    """
    The main shopping functionality
    """
    picked_store =pick_store()
    cart = Cart()
    pick_products(cart,picked_store)
    #cart.checkout()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
