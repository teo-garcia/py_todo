from menu import display
from tasks import add_task, remove_task, get_tasks
from utils import get_int


def main ():
  print("Welcome to PyTodo")

  # Display the menu options
  display()

  while True:
    choice = get_int("Enter your choice: ")
    if choice == 1:
      add_task()
    elif choice == 2:
      remove_task()
    elif choice == 3:
      get_tasks()
    elif choice == 4:
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()