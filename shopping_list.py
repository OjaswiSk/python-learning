shopping_list = []

while True:
    print("\n Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Quit")
    choice = input("Enter your choice (1-4):")

    if choice == "1":
        item = input("Enter the item to add:")
        shopping_list.append(item)
        print(f"{item} added")

    elif choice == "2":
        item = input("Enter the item to remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed")
        else:
            print(f"{item} not found in the list")

    elif choice == "3":
        if shopping_list :
            print("Shopping List:")
            for i, item in enumerate(shopping_list,1):
                print(f"{i}. {item}")
        else:
            print("Shopping List is empty")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")  
