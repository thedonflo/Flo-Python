import csv
import db
from objects import Task, TaskList

def display_task_list_names():
    names = db.get_task_listnames()
    print("TASK LISTS")
    cnt = 1
    for name in names:
        print(f"{cnt}. {name}")
        cnt += 1
    print()

choices =['list','add','complete','delete','exit']

def list_tasks(tasks):
    if tasks.getListCount() == 0:
        print("There are no tasks in this list.\n")
    else:
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1
    print()

def add_task(name, tasks):
    description = Task(input('Description: '))
    tasks.addTask(description)

def complete_task(tasks):
    number = int(input('Number: '))
    task = tasks.getTask(number)
    # print(task)
    # print(task.completed)
    task.completed = True
    return tasks

def delete_task(tasks):
    choice = int(input('Number: '))
    tasks.removeTask(choice - 1)


def show_menu():
    print("The Task List program")
    print("COMMAND MENU")
    print("list - List all task")
    print("add  - Add an task")
    print("complete  - Complete a task")
    print("delete  - Delete a task")
    print("exit - Exit program")
    print()




def main():
    show_menu()
    display_task_list_names()
    names = db.get_task_listnames()
    selection = int(input('Enter number to select task list: '))
    name = names[selection - 1]
    tasks = db.get_task_list(name)
    print(f"{name} task list was selected.")
    print()

    while True:
        choice = input('Command: ')
        if choice.lower() == "list":
            # print(db.get_task_list(tasks))
            # print(tasks)
            list_tasks(tasks)
        elif choice.lower() == "add":
            add_task(tasks)
            # current_list.addTask(description)
            # db.write_task_list(tasks, current_list)
        elif choice.lower() == "complete":
            complete_task(tasks)
        elif choice.lower() == "delete":
            delete_task(tasks)
        elif choice.lower() == "exit":
            db.write_task_list(name, tasks)
            print("Thanks for using our service")
            break
        else:
            print("Not a valid command. Please try again.\n")
        print()



if __name__ == "__main__":
    main()