# daily_reminder.py

# Step 1: Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process priority with match-case
print("Reminder:")

match priority:
    case "high":
        reminder = f"HIGH priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f" low priority task: {task}"
    case _:
        reminder = f"Task: {task} (Unknown priority level)"

# Step 3: Add urgency if time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Step 4: Display final reminder
print(reminder)

