if choice == '1':
    item = input("Enter item to add: ")
    shopping_list.append(item)
elif choice == '2':
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found.")
elif choice == '3':
    print("Current List:")
    for item in shopping_list:
        print(f"- {item}")
