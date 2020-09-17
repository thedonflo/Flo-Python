class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        complete = ""
        if self.completed == True:
            return self.description + " (DONE!)"
        return self.description + complete

class TaskList:
    def __init__(self,name):
        self.name = name
        self.__list = []


    def getListCount(self):
        return len(self.__list)

    def addTask(self, task):
        self.__list.append(task)

    def getTask(self, number):
        index = number - 1
        task = self.__list[index]
        return task

    def removeTask(self,task):
        self.__list.pop(task)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list) - 1:
            raise StopIteration
        self.__index += 1
        number = self.__list[self.__index]
        return number

    def __str__(self):
        name = ""
        for i in self.__list:
            name += f"{i} \n"
        name = name[:-1]
        return name


# task1 = Task('Pay bills')
# task2 = Task('Get groceries')
# tasks = TaskList()
# tasks.addTask(task1)
# tasks.addTask(task2)
# print(tasks)
