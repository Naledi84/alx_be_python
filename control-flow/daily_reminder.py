# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    full_message = f"Reminder: {base_message} that requires immediate attention today!"
elif time_bound == "no":
    full_message = f"Note: {base_message}. Consider completing it when you have free time."
else:
    full_message = f"{base_message}. Time sensitivity not specified."

# Output the customized reminder
print(full_message)

