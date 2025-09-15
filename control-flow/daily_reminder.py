# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify message based on time sensitivity
if time_bound == "yes" and "Reminder" in message:
    message += " that requires immediate attention today!"
elif time_bound == "no" and "Note" in message:
    message += ". Consider completing it when you have free time."

# Output the customized reminder
print(message)
