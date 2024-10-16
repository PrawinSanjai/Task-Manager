import json

tasks = []
users = {}

def load_users(filename='users.json'):
    global users
    try:
        with open(filename, 'r') as file:
            users = json.load(file)
        print("Data loaded.")
    except FileNotFoundError:
        print("No existing users found.")

def save_users(filename='users.json'):
    with open(filename, 'w') as file:
        json.dump(users, file)
    print("Data saved.")

def load_tasks(filename='tasks.json'):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            tasks = tasks_data.get(current_user, [])
        print("Tasks loaded for user:", current_user)
    except FileNotFoundError:
        print("No tasks found.")

def save_tasks(filename='tasks.json'):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
    except FileNotFoundError:
        tasks_data = {}
    
    tasks_data[current_user] = tasks
    with open(filename, 'w') as file:
        json.dump(tasks_data, file)
    print("Tasks saved.")

def login():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    if user_id in users and users[user_id] == password:
        print("Login successful!")
        return user_id
    else:
        print("Invalid User ID or Password. Please try again.")
        return None

def register():
    user_id = input("Create your User ID: ")
    if user_id in users:
        print("User ID already exists. Please try another one.")
        return None
    
    password = input("Create your Password: ")
    users[user_id] = password
    save_users()
    print(f"User '{user_id}' registered successfully!")
    return user_id

def add_task(title):
    task_id = len(tasks) + 1
    task = {"id": task_id, "title": title, "completed": False}
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task with ID {task_id} deleted.")

def mark_task_complete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task ID {task_id} marked as completed.")
            break
    else:
        print(f"No task found with ID {task_id}")

def main():
    global current_user

    load_users()

    while True:
        print("\nWelcome to Task Manager")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            current_user = login()
            if current_user:
                break
        elif choice == '2':
            current_user = register()
            if current_user:
                break
        elif choice == '3':
            print("Exiting the program.")
            return
        else:
            print("Invalid option, please try again.")

    load_tasks()

    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == '5':
            save_tasks()
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    current_user = None
    main()
