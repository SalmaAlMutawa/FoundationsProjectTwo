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
    print ("Please choose a store: \n")
    for store in stores:
        print ("> %s" % store.name)
    print ("\nPlease choose a store name.")

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    usr_inp = False
    while usr_inp == False:
        usr_inp = input()
        if usr_inp.lower() == "checkout":
            return "checkout"

        store_obj = get_store(usr_inp)
        if store_obj != False:
            print("\nThank you for choosing %s" % store_obj.name)
            return store_obj

        print("Sorry invalid store, please try again: ")
        usr_inp = False

    # return get_store(choice)
 
def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    print ("Enter \"back\" to go to the main menu, or \"checkout\" to exit.")
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    user_choice = input("Choose your product: ")
    while user_choice != "back":
        if user_choice == "checkout":
            return "checkout"

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

    return "back"
    



def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    picked_store = ""
    while picked_store != "checkout":
        picked_store = pick_store()
        if picked_store == "checkout":
            break

        option = pick_products(cart,picked_store)
        if option.lower() == "checkout":
            break

    cart.checkout()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
