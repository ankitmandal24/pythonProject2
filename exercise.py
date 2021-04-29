#  excersie 1
birth_year = input('year you born')
present_year = input('present year')
age = int(present_year) - int(birth_year)
print(f'your age is {age}')

#  password checker
username = input('type username')
password = input('type password')
here = len(password)
hidden_password = '*' * here
print(f' your username is {username} and password is {hidden_password} which is {here} letters  long')
