def is_prime(num):
#
# Write your code here.
    if (num ** 0.5).is_integer():
        return False
    for i in range(2, num+1):
        if num % i == 0 and num != i:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
