from utils import get_int, get_string

tasks = []

def add_task():
  new_task = get_string("Enter a task: ")
  tasks.append(new_task)
  print("Task added successfully!")

def remove_task():
  if not tasks:
    return
  
  get_tasks()

  choice = get_int("Enter the task id to remove") - 1

  if choice <= 0 or choice >= len(tasks):
    print("Invalid task number.")
  else:
    removed_task = tasks.pop(choice)
    print(f"Task {removed_task} removed successfully.")


def get_tasks():
  if not tasks:
    print("No tasks available.")
    return
  print("Current Tasks:")
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")