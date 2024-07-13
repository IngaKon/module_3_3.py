def print_params(a = 1, b = 'строка', c = True):
    #print (a,b,c,f)#Лишний аргумент приводит у ошибке.
    print(a,b,c)
print_params(b = 25)
print_params(c = [1,2,3])
 #Распаковка параметров:
values_list=['Вера',[4,8,5],True]
values_dict={'a':24,'b':'Morgan','c':['деньги','окно','работа']}
print_params(*values_list)
print_params(**values_dict)
 #Распаковка + отдельные параметры:
values_list_2=[54.32, 'Строка' ]
print_params(*values_list_2, 42)

