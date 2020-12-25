#  formatted strings

name = 'ironman'
age = 32

print(f'hi {name} you are {age} years old')

# also we can write this in number format

print('hi {0} you are {1} years old'. format(name, age))

#  string indexes
selfish = '1234567'

#  [start:stop:stepover]
print(selfish[0:7:2])
print(selfish[::-1])
print(selfish[-1])  # -ve means reverse

