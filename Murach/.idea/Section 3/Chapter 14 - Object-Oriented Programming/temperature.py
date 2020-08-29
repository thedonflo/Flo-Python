class Temp():
    def __init__(self):
        self.__celcius = 0
        self.__fahrenheit = 32

    def setCelsius(self,celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius * 9/5 + 32

    def setFahrenheit(self,fahrenheit):
        self.__fahrenheit = fahrenheit
        self.__celcius = (fahrenheit - 32) * 5/9

    def getCelsius(self,celsius):
        return round(self.__celcius, 2)

    def getFahrenheit(self, fahrenheit):
        return round(self.__fahrenheit, 2)




# def to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius
#
# def to_fahrenheit(celsius):
#     fahrenheit = celsius * 9/5 + 32
#     return fahrenheit

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    temp = Temp()
    for f in range(0, 212, 40):
        temp.setFahrenheit(f)
        print(f, "Fahrenheit equals", temp.getCelsius(f), "Celsius")

    for c in range(0, 100, 20):
        temp.setCelsius(c)
        print(c, "Celsius equals", temp.getFahrenheit(c), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

