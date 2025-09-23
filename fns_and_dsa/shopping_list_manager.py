import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    future = datetime.datetime.now() + datetime.timedelta(days=days)
    return future.strftime("%Y-%m-%d")

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
