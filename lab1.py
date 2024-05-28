# Key programming activities in a simple to-do list manager

# Function to display menu
def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

# Function to add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- All Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{i}. {task['task']} - {status}")

# Function to mark a task as complete
def mark_task_complete(tasks):
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
