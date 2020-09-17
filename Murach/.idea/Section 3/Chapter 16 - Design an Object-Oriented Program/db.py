import csv
from objects import Task, TaskList

# CSV names are "personal.csv" and "business.csv"

def get_task_listnames():
    task_lists = []
    filename = "task_list"
    with open(filename) as file:
        for line in file:
            line = line.replace('\n','')
            task_lists.append(line)
        return task_lists

def get_task_list(name):
    filename = name.lower() + ".csv"
    tasks = TaskList(name)
    with open(filename, newline="",) as file:
        reader = csv.reader(file)
        # next(reader, None) #skip the headers
        for row in reader:
            # convert row into tasks
            task = Task(row[0],row[1])
            tasks.addTask(task)
        return tasks

def write_task_list(name, tasks):
    rows = []
    for task in tasks:
        row = []
        row.append(task.description)
        row.append(task.completed)
        rows.append(row)

    #Write to csv
    filename = name.lower() + ".csv"
    with open(filename, "w",newline="",) as file:
        writer = csv.writer(file)
        writer.writerows(rows)


# Code that test database and business layers
# def main():
    # print(get_task_listnames())
    # task_lists = get_task_list("personal")
    # print("Printing Current List")
    # print(task_lists)
    # task1 = Task("Buy toothbrush")
    # task2 = Task("Do homework")
    # task_lists.addTask(task1)
    # task_lists.addTask(task2)
    # print()
    # print("List after creating TaskList objects")
    # print(task_lists)
    # print()
    # print("Writing TaskList objects to csv file")
    # write_task_list("personal",task_lists)

# if __name__ == "__main__":
#     main()



