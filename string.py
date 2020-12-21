print(type('hi ankit here '))  # "hi ankit here" it is also valid string
username = 'ironman'
password = '24'

long_string = '''  # for long string 
wow
0 0
___
'''
print(long_string)

first_name = 'ankit'
last_name = 'mandal'
full_name = first_name+last_name
print(full_name)
# for space use string
full_name = first_name + ' ' + last_name
print(full_name)
#  string concatenation means adding two strings
print('hello' + ' people')

# type conversion
print(type(int(str(100))))   #  also we can write int this form (see below)
a = str(100)
b = int(a)
c = type(b)
print(c)
#  Escape sequence
weather = "\t It's \"kind of\" sunny \n hope u have nice day"
#  \t for tab(double space) & \n for new line
print(weather)
