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

#  built in function
greet = 'helllllooooo'
print(greet[0:len(greet)])

quote= 'to be or not to be'
print(quote.upper())  #  written in all capital and use .lower for all capital
print(quote.capitalize())
print(quote.find('not'))
print(quote.replace('to','me'))

print(quote) # it is immutability which mean they never gonna change we just overwrite it until we change the sentence

#  booleans

name = 'minions'
name = False
is_ok = False
is_ok = True

print(bool(0))

