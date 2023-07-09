def addDish(menu):
    try:
        id = int(input("\nEnter id: "))
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        availability = input("Is dish available? (yes/no): ")
        pieces = 0

        if availability == "yes":
            pieces = int(input("Enter available quantity of dish: "))

        dish = {}
        dish["id"] = id
        dish["name"] = name
        dish["price"] = price
        dish["availability"] = availability
        dish["pieces"] = pieces

        menu.append(dish)
        print(f"\nNew dish {name} is added to menu.")

    except ValueError:
        print("\nInvalid input. Please enter a valid value!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


def removeDish(menu):
    try:
        id = int(input("\nEnter id: "))

        i = 0
        for dish in menu:
            if dish["id"] == id:
                print(f"\nDish ({dish['name']}) removed from the menu.")
                menu.pop(i)
                return
            i += 1
        
        print(f"\nDish not found with id: {id}")

    except Exception as e:
        print("\nAn error occurred:", str(e))




def updateAvailability(menu):
    try:
        id = int(input("\nEnter id: "))

        for dish in menu:
            if dish["id"] == id:
                availability = input("\nIs the dish available? (yes/no): ")
                dish["availability"] = availability

                if availability == "no":
                    dish["pieces"] = 0
                else:
                    pieces = int(input("\nEnter available quantity of dish: "))
                    dish["pieces"] = pieces

                print("\nDish availability updated")
                return
        
        print(f"\nDish not found with id: {id}")

    except Exception as e:
        print("\nAn error occurred:", str(e))
    


def viewMenu(menu):
    print("\n====== Menu ======")
    if len(menu) == 0:
        print("Any dish is not available!")
    else:
        print(f"Id  \t  Name  \t  price  \t  Available  \t  Pieces")
        for dish in menu:
            print(f"{dish['id']}  \t  {dish['name']}  \t  {dish['price']}  \t\t  {dish['availability']}  \t\t  {dish['pieces']}")

    


def takeOrder(menu,orderList):
    try:
        oId = int(input("\nEnter order id: "))
        name = input("Enter customer name: ")
        id = int(input("Enter dish id: "))
        flag = True

        for dish in menu:
            if dish["id"] == id:
                flag = False
                if dish["availability"] == "no":
                    print(f"Sorry, dish with id {id} is not available!")
                    return
                else:
                    dish["pieces"] = dish["pieces"] - 1
        
        if flag: 
            print(f"Not found any dish with id {id}")
            return

        order = {}
        order["oId"] = oId
        order["cusName"] = name
        order["dishId"] = id
        order["status"] = "received"

        orderList.append(order)
        print(f"\nNew order is received.")

    except ValueError:
        print("\nInvalid input. Please enter a valid value!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


    
def updateOrderStatus(orderList):
    try:
        oId = int(input("\nEnter order id: "))

        for order in orderList:
            if order["oId"] == oId:
                status = input("Enter order status: ")
                order["status"] = status

        print(f"\norder status is changed.")

    except ValueError:
        print("\nInvalid input. Please enter a valid value!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


    
def viewOrder(orderList):
    for order in orderList:
        print(order)













def main():
    menu = []
    order = []

    while True:
        print("\n====== Welcome to Zomato Chronicles ======")
        print("1. Add a dish")
        print("2. Remove a dish")
        print("3. Update dish availability")
        print("4. View menu")
        print("5. Take a order")
        print("6. Update order status")
        print("7. View order")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            addDish(menu)
        elif choice == '2':
            removeDish(menu)
        elif choice == '3':
            updateAvailability(menu)
        elif choice == '4':
            viewMenu(menu)
        elif choice == '5':
            takeOrder(menu,order)
        elif choice == '6':
            updateOrderStatus(order)
        elif choice == '7':
            viewOrder(order)
        elif choice == '0':
            print("\nThanks for using our service!")
            break
        else:
            print("\nInvalid choice. Please try again.")






main()



