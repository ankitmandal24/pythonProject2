# dictionary
fame= {'a': [1,2,3],
       'b': 'ok',
       'c': 'hello'}
#print(dict['a'][0])

my_list=[{'a': [1,2,3],
       'b': 'ok',
       'c': 'hello'},
         {'a': [4, 5, 6],
          'b': 'ok',
          'c': 'hello'}
         ]
#print(my_list[1]['a'][2])

user = {'basket': [1,2,3],
        'greet': 'hello',
        'age':20}
#print(user.get('age',55))  #  it is used to find whether the key present or not
user2 = dict(name ='ak')  #  add key and value
print(user2)

print('hello' in user) # tells whether key exist or not

print(user.popitem())

