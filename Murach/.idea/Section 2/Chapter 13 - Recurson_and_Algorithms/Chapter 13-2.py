# In this exercise, you ' 11 test the Towers of Hanoi puzzle.
# Open and test the program
# 1. In IDLE, open the towers_of_hanoi.py file that's in this folder:
# python/ exerc ises/ ch13
# 2. Review the code and run it for 3, 4, and 5 disks. Note that the pattern is
# slightly different depending on whether the number is even or odd.
# 3. Continue testing with larger numbers until the program begins running too
# slowly to be acceptable.
# Add a print statement that traces the calls on the stack
# 4. Add a statement to the start of the move_disk() function that prints the name
# of the function and the values of the arguments that are being passed to it.
# When you 're done, the console should look like this for 4 disks:
# **** TOWERS OF HANOI****
# E.nter number of disks: 4
# move_disk (n=4, src=A, dest=C, temp=B )
# move_disk (n=3, src=A, dest=B, temp=C )
# move_disk (n=2, src=A, dest=C, temp=B )
# move_disk (n=l, src =A, dest=B, temp=C )
# move_disk (n=O, src=A, dest=C, temp=B )
# Move disk 1 from A to B
# move_disk (n=O, src=C, dest=B, temp=A)
# Move disk 2 from A to C
# move_disk (n=l, src=B, dest=C, temp=A)
# move_disk (n=O, src=B, dest=A, temp=C )
# Move disk 1 from B to C
# move_disk (n=O, src=A, dest=C, temp=B )
# Move disk 3 from A to B
# move_disk (n=2, src=C, dest=B, temp=A)
# move_disk (n=l, src=C, dest=A, temp=B )
# move_disk (n=O, src=C, dest=B, temp=A)
# •••
# 5. Study the console and note how the move_disk() functions are pushed onto
# the stack and popped off the stack.

#!/usr/bin/env python3

def move_disk(n, src, dest, temp):
    print("    move_disk(n={:d}, src={:s}, dest={:s}, temp={:s})"
          .format(n, src, dest, temp))
    if n == 0:
        return
    else:
        move_disk(n-1, src, temp, dest)
        print("Move disk", n, "from", src, "to", dest)
        move_disk(n-1, temp, dest, src)

def main():
    print("**** TOWERS OF HANOI ****")
    print()
    num_disks = int(input("Enter number of disks: "))
    print()

    move_disk(num_disks, "A", "C", "B")

    print()
    print("All disks have been moved.")

if __name__ == "__main__":
    main()