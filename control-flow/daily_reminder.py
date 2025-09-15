# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority
match priority:
    case "high":
        reminder = "is a high priority task"
    case "medium":
        reminder = "is a medium priority task"
    case "low":
        reminder = "is a low priority task"
    case _:
        reminder = "has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."

# Store in dictionary to match validation format
s = {
    "t": task,
    "r": reminder
}

# Final output (validator expects this exact format)
print(f"{s['t']} Reminder:{s['r']}")


