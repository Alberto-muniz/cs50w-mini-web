def show_menu():
    print("1- add product")
    print("2 - show cart")
    print("3 - Show total")
    print("4 - Checkout finished")
    print("5 - Exit")

def add_product(products):
        name = input("Product name: ")
        price = int(input("Product price: "))

        product = {
            "name": name,
            "price": price 
        }
        

        products.append(product)
        print("product added successfully.")


def show_products(products):
    if len(products) == 0:
        print("No products in cart.")
        return
    
    for product in products:
        print(product["name"], "-", product["price"])

def show_total(products):
    if len(products) == 0:
        print("No productos in cart.")
        return

    total = 0
    for product in products:
        total += product["price"]

    print("total", total)


def show_checkout(products):
        if len(products) == 0:
         print("No products to checkout")
         return
    
    
        show_total(products)
        products.clear()
        print("Sale completed.")


def main():
    products = []

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            add_product(products)
        elif option == "2":
            show_products(products)
        elif option == "3":
            show_total(products)
        elif option == "4":
            show_checkout(products)
        elif option == "5":
            print("goodbye!")
            break
        else:
            print("invalid option")



main()


