class Book:
    def __init__(self, title="", authors=None):
        self.title = title
        self.authors = authors

    def getDescription(self):
        return self.title + " by " + self.authors

    def __str__(self):
        return self.title + " by " + str(self.authors)
                
class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return self.firstName+' '+self.lastName

class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        name = ""
        for i in self.__list:
            name += str(i) + ', '
        name = name[:-2]
        return name

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list)- 1:
            raise StopIteration
        self.__index += 1
        number = self.__list[self.__index]
        return number




author1 = Author("Mark", "Twain")
author2 = Author("Charles", "Warner")
authors = Authors()
authors.add(author1)
authors.add(author2)
for name in authors:
    print(name)