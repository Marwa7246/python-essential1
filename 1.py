for i in range(2,8):
    print("The value of i is currently", i)

# Store the current largest number here.

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
largest_number = number

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)
print (0==True)

#The way we've used it here is called multi-line printing. You can use triple quotes to print strings on multiple lines in order #to make text easier to read, or create a special text-based design. Experiment with it.

# secret code, infinite loop
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
x = int(input("Enter an integer number: "))

while x != secret_number:
    print ("Ha ha! You're stuck in my loop!")
    x = int(input("Enter an integer number: "))
print (str(x) + "!!!, Well done, muggle! You are free now.")