def print_params_(a=1, b='строка', c=True):
    print (a,b,c)
print_params_()
print_params_(b=25)
print_params_(c=[1,2,3])
values_list=[25,'happiness',True]
values_dict={'a':1, 'b':"строка", 'c':True}
print_params_(*values_list)
print_params_(**values_dict)
values_list_2=[54.32,'Строка']
print_params_(*values_list_2,42)