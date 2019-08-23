import temperature

def main():
    for temp in range(0, 212, 40):
        print(temp, "Farenheit =", round(temperature.to_celsius(temp), 2), "Celsius")
    print("*" * 40)
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(temperature.to_fahrenheit(temp), 2),
              "Fahrenheit")

if __name__ == "__main__":
    main()



