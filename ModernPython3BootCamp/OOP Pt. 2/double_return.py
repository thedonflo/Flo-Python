# double_return
# Write a function called double_return which accepts a function and returns another function.
# double_return should decorate a function by returning two copies of the inner function's return value inside of a list

# from functools import wraps


def double_return(fn):
    # @wraps(fn)
    def wrapper(*args, **kwargs):
        # build = [fn(*args, **kwargs), fn(*args, **kwargs)]
        build = []
        for i in range(2):
            build.append(fn(*args, **kwargs))
        return build
    return wrapper


@double_return
def add(x, y):
    return x + y

print(add(1, 2)) # [3, 3]


@double_return
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]

