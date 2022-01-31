# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

vals=[0,1,2]
vals[0], vals[1] = vals[1], vals[2]
print(vals)

my_list=[222 for i in range(-1,2)]
print (my_list)

var =1
while var < 10:
    print("#")
    var = var << 1
    print (var)

my_list=[1,2,3,4]
print (my_list[-3:-2])

my_list=[1,2,3]

for v in range(len(my_list)):
    print(v, (my_list))
    my_list.insert(1,my_list[v])
print (my_list)


def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
