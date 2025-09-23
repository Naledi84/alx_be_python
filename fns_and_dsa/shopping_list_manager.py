# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter a number (1-4).")
            continue

        if choice == 1:
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to the shopping list.")
            else:
                print("⚠️ Item cannot be empty.")
        
        elif choice == 2:
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")
        
        elif choice == 3:
            # View list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is currently empty.")
        
        elif choice == 4:
            print("👋 Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
