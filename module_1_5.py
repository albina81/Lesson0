immutable_var=1, 2, 3, True, 'job'
print (immutable_var)
immutable_var=(1, 2, 3, True, 'job')
print (immutable_var)
immutable_var=([1, 2, 3, True, 'job'])
print (immutable_var)

immutable_var=1, 2, 3, True, 'job'
print (immutable_var)
print(type(immutable_var))
print('Кортеж (tuple) не поддерживает обращение по элементам, потому что это неизменяемый список')
immutable_var[2] = 8
print (immutable_var)

Mutable_list=[1, 2, 'a', 'b', 'Modified']
Mutable_list[3]=7
print(Mutable_list)