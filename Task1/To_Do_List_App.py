import os

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{idx}. {task.title} - {task.description} ({status})")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    title, description, completed = parts
                    tasks.append(Task(title, description, completed == "True"))
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task.title}|{task.description}|{task.completed}\n")

def main():
    todo_list = ToDoList()
    todo_list.tasks = load_tasks()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("======================")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            save_tasks(todo_list.tasks)
            input("Task added. Press Enter to continue.")

        elif choice == '2':
            task_title = input("Enter the title of the task to remove: ")
            todo_list.remove_task(task_title)
            save_tasks(todo_list.tasks)
            input("Task removed. Press Enter to continue.")

        elif choice == '3':
            task_title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_completed(task_title)
            save_tasks(todo_list.tasks)
            input("Task marked as completed. Press Enter to continue.")

        elif choice == '4':
            todo_list.display_tasks()
            input("Press Enter to continue.")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()
