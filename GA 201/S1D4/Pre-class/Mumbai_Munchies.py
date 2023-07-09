def addSnack(inventory):
    try:
        id = input("\nEnter id: ")
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        availability = input("Is snack available? (yes/no): ")

        snack = {}
        snack["id"] = id
        snack["name"] = name
        snack["price"] = price
        snack["availability"] = availability

        inventory.append(snack)
        print("\nSnack added!")

    except ValueError:
        print("\nInvalid input. Please enter a valid value!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


def removeSnack(inventory):
    try:
        id = input("\nEnter id: ")

        i = 0
        for snack in inventory:
            if snack["id"] == id:
                inventory.pop(i)
                print("\nSnack removed from the inventory.")
                return
            i += 1
        
        print(f"\nSnack not found with {id}")

    except Exception as e:
        print("\nAn error occurred:", str(e))



def updateAvailability(inventory):
    try:
        id = input("\nEnter id: ")

        for snack in inventory:
            if snack["id"] == id:
                availability = input("\nIs the snack available? (yes/no): ")
                snack["availability"] = availability
                print("\nSnack availability updated")
                return
        
        print(f"\nSnack not found with {id}")

    except Exception as e:
        print("\nAn error occurred:", str(e))


def soldSnack(inventory, saleRecord):
    try:
        id = input("\nEnter snack ID sold: ")

        i = 0
        for snack in inventory:
            if snack["id"] == id:
                if snack["availability"] == 'yes':
                    saleRecord.append(snack)
                    inventory.pop(i)
                    print("\nSnack sold!")
                    return
                else:
                    print("\nSnack is not available")
                    return
            i += 1
        
        print(f"\nSnack not found with {id}")

    except Exception as e:
        print("\nAn error occurred:", str(e))


def viewInventory(inventory):
    print("\n====== Inventory ======")
    for snack in inventory:
        print(f"Snack ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {snack['availability']}")



def viewSoldSnack(saleRecord):
    print("\n====== Sales Record ======")
    for snack in saleRecord:
        print(f"Snack ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}")



def main():
    inventory = []       
    saleRecord = []    

    while True:
        print("\n====== Mumbai Munchies =======")
        print("1. Add a snack")
        print("2. Remove a snack")
        print("3. Update snack availability")
        print("4. sale recode")
        print("5. Display inventory")
        print("6. Display sale record")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            addSnack(inventory)
        elif choice == '2':
            removeSnack(inventory)
        elif choice == '3':
            updateAvailability(inventory)
        elif choice == '4':
            soldSnack(inventory, saleRecord)
        elif choice == '5':
            viewInventory(inventory)
        elif choice == '6':
            viewSoldSnack(saleRecord)
        elif choice == '0':
            print("\nThanks for using our service!")
            break
        else:
            print("\nInvalid choice. Please try again.")


main()




