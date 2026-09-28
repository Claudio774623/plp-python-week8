# Personal Mini-Toolkit

# This program provides three simple tools:

# a number guessing game, a to-do list, and a calculator.

# Tool 1: Number Guessing Game

# This tool asks the user to guess a secret number until they get it correct.

def number_guessing_game():
secret_number = 7
attempts = 0

```
print("\n--- Number Guessing Game ---")
print("I have chosen a number between 1 and 10.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(f"Your guess {guess} is too low. Try again.")
        elif guess > secret_number:
            print(f"Your guess {guess} is too high. Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a whole number from 1 to 10.")
```

# Tool 2: To-Do List

# This tool allows the user to add, view, and remove tasks from a list.

def todo_list():
tasks = []

```
print("\n--- To-Do List ---")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Return to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' has been added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to remove.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' has been removed.")
                else:
                    print("That task number does not exist.")

            except ValueError:
                print("Please enter a valid task number.")

    elif choice == "4":
        print("Returning to the main menu.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
```

# Tool 3: Simple Calculator

# This tool performs basic mathematical calculations.

def calculator():
print("\n--- Simple Calculator ---")

```
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice: ")

    if operation == "1":
        result = first_number + second_number
        print(f"The answer is {result}.")

    elif operation == "2":
        result = first_number - second_number
        print(f"The answer is {result}.")

    elif operation == "3":
        result = first_number * second_number
        print(f"The answer is {result}.")

    elif operation == "4":
        if second_number == 0:
            print("You cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"The answer is {result}.")

    else:
        print("Invalid operation. Please choose 1, 2, 3, or 4.")

except ValueError:
    print("Please enter valid numbers.")
```

# Main menu

# This loop keeps the toolkit running until the user chooses Quit.

print("============================================")
print("     Welcome to My Personal Mini-Toolkit")
print("============================================")

while True:
print("\n========== PERSONAL MINI-TOOLKIT ==========")
print("1. Number Guessing Game")
print("2. To-Do List")
print("3. Simple Calculator")
print("4. Quit")
print("============================================")

```
choice = input("Enter your choice: ")

if choice == "1":
    number_guessing_game()

elif choice == "2":
    todo_list()

elif choice == "3":
    calculator()

elif choice == "4":
    print("\nThank you for using my Personal Mini-Toolkit!")
    print("Goodbye!")
    break

else:
    print(f"Sorry, '{choice}' is not a valid choice.")
    print("Please choose 1, 2, 3, or 4.")
```

1
7
20