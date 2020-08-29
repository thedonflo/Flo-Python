class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getStr(self):
        return f"{self.name} ({self.year})"

movie = Movie('Car',2012)
print(movie.getStr())