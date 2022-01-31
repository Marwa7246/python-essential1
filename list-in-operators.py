# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
new_list = my_list[0:1]
for ele in my_list:
    if ele not in new_list:
        new_list.append(ele)
my_list=new_list[:]
#

print("The list with unique elements only:")
print(new_list)