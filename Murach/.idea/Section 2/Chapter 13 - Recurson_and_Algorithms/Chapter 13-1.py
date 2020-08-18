# In this exercise, you ' 11 test the recursive function that prints part of the
# Fibonacci series. Then, you '11 test an iterative function that does the same thing,
# but more efficiently.
# Open and test the recursive Fibonacci program
# 1. In IDLE, open the fibonacci_recursion.py file that's in this folder:
# python/ exerc ises/ ch13
# 2. Review the code and run it to make sure it works correctly. It should print the
# first 16 numbers of the Fibonacci series.
# 3. Modify the code so it calculates a Fibonacci series for 32 numbers, and run it
# again. Note how slowly it runs.
# View the stack for the program
#     4. Modify the code so it calculates a Fibonacci series for 100 numbers, and run it
# again. While it's running press Ctrl+C on a Windows system or Co1runand+C
# on a Mac to interrupt the calculation and view the stack trace. Note that the
# fib () function has been placed on the stack numerous times.
# 5. From the IDLE shell, select Debug7 Stack Viewer. In the Stack Viewer,
# expand a few of the fib() functions and note that they include the values for
#     the local variable named n.
# Open and test the iterative Fibonacci program
# 6. Open the fibonacci_loop.py file that's in the same folder.
# 7. Review the code and run it to make sure it works correctly.
# 8. Modify the code so it calculates a Fibonacci series for 100 numbers, and run
# it. Note how quickly it runs compared to the recursive program.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    for i in range(100):
    # for i in range(16):
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()
