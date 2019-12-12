'''
Writing Your Own Lambda!
Write a lambda that accepts a single number and cubes it. Save it in a variable called cube .

cube(2)  # 8

cube(3)  # 27

cube(8)  # 512

This challenge has tests ensuring that cube  is a lambda rather than a function, so don't cheat and make it a plain old function :)

# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
'''
cube = lambda x: x**3

print(cube(8))