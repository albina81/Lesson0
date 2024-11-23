my_dict={'Vasya':1975, 'Egor':1999, 'Masha':2002}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Kamila'))
my_dict.update({'Kamila':1981,
               'Artem':1985})
a=my_dict.pop('Egor')
print(a)
print(my_dict)
#работа с множествами
my_set={1,'Яблоко',42.314,'Яблоко'}
print(my_set)
my_set.add((5,7,1.6))
my_set.add(16)
my_set.remove(1)
print(my_set)