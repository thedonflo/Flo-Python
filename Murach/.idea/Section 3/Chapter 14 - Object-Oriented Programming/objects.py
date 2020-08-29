class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getStr(self):
        return self.name + " ("  + str(self.year) + ")"