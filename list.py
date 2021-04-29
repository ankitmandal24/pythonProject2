my_list = ['apple',
           'banana',
           'kiwi',
           'orange']  # list slicing
print(my_list[1::2])
my_list[1] = 'ok'
new_list = my_list[:]  # only copy
new_list[1] = 'cucumber'
print(new_list)
print(my_list)

#  matrix
matrix = [
    [0,1,2],
    [2,3,1],
    [4,5,6]
]
print(matrix[2][2])
