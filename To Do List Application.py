import os

# Initialize an empty to-do list
tasks = []

# Function to display the menu and get user choice
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Quit")
    choice = input("Enter your choice (1-7): ")
    return choice

# Function to add a task to the list
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"Title": title, "Description": description, "Complete": False}
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = "Complete" if task["Complete"] else "Incomplete"
            print(f"{index + 1}. Title: {task['Title']}, Description: {task['Description']}, Status: {status}")

# Function to mark a task as complete or incomplete
def mark_task():
    list_tasks()
    index = int(input("Enter the task number to mark as complete/incomplete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["Complete"] = not tasks[index]["Complete"]
        print("Task status updated successfully!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    list_tasks()
    index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['Title']},{task['Description']},{task['Complete']}\n")
    print("Tasks saved to 'tasks.txt'.")

# Function to load tasks from a text file
def load_tasks():
    global tasks
    if os.path.exists("tasks.txt"):
        tasks = []
        with open("tasks.txt", "r") as file:
            for line in file:
                title, description, complete = line.strip().split(",")
                tasks.append({"Title": title, "Description": description, "Complete": complete == "True"})
        print("Tasks loaded from 'tasks.txt'.")
    else:
        print("No saved tasks found.")

# Main loop
while True:
    choice = display_menu()

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        load_tasks()
    elif choice == "7":
        print("Thank you for using the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-7).")
