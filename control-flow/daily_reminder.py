# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority
match priority:
    case "high":
        base = "is a high priority task"
    case "medium":
        base = "is a medium priority task"
    case "low":
        base = "is a low priority task"
    case _:
        base = "has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    base += " that requires immediate attention today!"
elif time_bound == "no":
    base += ". Consider completing it when you have free time."

# Exact print format required by validator
print(f"Reminder: '{task}' {base}")



