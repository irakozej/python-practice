import requests

base_url = 'http://127.0.0.1:5000/tasks'

def print_tasks():
    response = requests.get(base_url)
    if response.status_code == 200:
        tasks = response.json().get('tasks', [])
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Done: {task['done']}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")

def create_task(title):
    new_task = {'title': title}
    response = requests.post(base_url, json=new_task)
    if response.status_code == 201:
        print(f"Task created: {response.json().get('task', {})}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")
def update_task(task_id, title, done):
    updated_task = {'title': title, 'done': done}
    response = requests.put(f'{base_url}/{task_id}', json=updated_task)
    if response.status_code == 200:
        print(f"Task updated: {response.json().get('task', {})}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")

def delete_task(task_id):
    response = requests.delete(f'{base_url}/{task_id}')
    if response.status_code == 200:
        print(f"Task deleted: {response.json().get('result', False)}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error')}")

# Add other CRUD functions as needed...

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Print Tasks")
        print("2. Create Task")
        print("3. Exit")
        print("4. update task")
        print("5. delete the task")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if choice == "1":
            print_tasks()
        elif choice == "2":
            title = input("Enter the task title: ")
            create_task(title)
        elif choice == "3":
            print("Exiting the program.")
        elif choice == "4":
            task_id = input("Enter ID of task you want to update: ")
            title = input("Enter new title: ")
            done = input("Enter whether the task is done (True/False): ")
            update_task(int(task_id), title, bool(done.lower() == 'true'))
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
