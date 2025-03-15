import os

"""A To-Do List application is a useful project that helps users manage
 and organize their tasks efficiently. This project aims to create a
 command-line or GUI-based application using Python, allowing
 users to create, update, and track their to-do lists
"""
def display_menu():
    print("To-Do List Application")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Mark a task as done")
    print("5. Mark a task as undone")
    print("6. Exit")

def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    return []

def save_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        file.write("\n".join(tasks))

def main():
    tasks = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tasks_file_path = os.path.join(script_dir, "tasks.txt")
    tasks = load_tasks(tasks_file_path)

    while True:
        display_menu()
        menu_option = input("Choose a menu option: ")

        if menu_option == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully.")
            save_tasks(tasks_file_path, tasks)
        elif menu_option == "2":
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task}' deleted successfully.")
                save_tasks(tasks_file_path, tasks)
            else:
                print("Invalid task index.")
        elif menu_option == "3":
            print("Task List:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
        elif menu_option == "4":
            task_index = int(input("Enter the index of the task to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index] += " [Done]"
                print(f"Task '{tasks[task_index]}' marked as done.")
                save_tasks(tasks_file_path, tasks)
            else:
                print("Invalid task index.")
        elif menu_option == "5":
            task_index = int(input("Enter the index of the task to mark as undone: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index] = tasks[task_index].replace(" [Done]", "")
                print(f"Task '{tasks[task_index]}' marked as undone.")
                save_tasks(tasks_file_path, tasks)
            else:
                print("Invalid task index.")
        elif menu_option == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid menu option.")

if __name__ == "__main__":
    main()

