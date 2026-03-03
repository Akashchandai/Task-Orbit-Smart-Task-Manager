import os

tasks = []

# Load tasks from file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip().split("|")
                tasks.append({
                    "id": int(task[0]),
                    "name": task[1],
                    "priority": task[2],
                    "status": task[3]
                })

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['name']}|{task['priority']}|{task['status']}\n")

# Add task
def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    task_id = len(tasks) + 1
    tasks.append({
        "id": task_id,
        "name": name,
        "priority": priority,
        "status": "Pending"
    })
    save_tasks()
    print("Task added successfully!")

# View tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"ID: {task['id']} | Name: {task['name']} | Priority: {task['priority']} | Status: {task['status']}")

# Update task status
def update_task():
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks()
            print("Task updated!")
            return
    print("Task not found!")

# Delete task
def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted!")
            return
    print("Task not found!")

# Main Menu
def menu():
    load_tasks()
    while True:
        print("\n==== PyTask Orbit ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting PyTask Orbit...")
            break
        else:
            print("Invalid choice!")

menu()