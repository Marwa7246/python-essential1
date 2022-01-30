# Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

for digit in "0165031806510":
    if digit == "0":
        digit = "x" # Line of code.
        continue # Line of code.
    print(digit, end="") # Line of code.

n = range(4)

for num in n:
    print(num - 1)
# else:
#     print(num)