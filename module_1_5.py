immutable_var =  (1, 51, 'учеба', 'работа')
print (immutable_var)
# immutable_var [2] = 10 если мы изменяем этот элемент, например, на число 10, и  выводим кортеж на экран,
# то столкнемся с ошибкой, так как кортедж нельзя изменять, а если в кортеже будет список то список в кортеже можно изменить
mutable_list = [1, 31, "жд", "вывод", True]
print (mutable_list)
mutable_list [1] = False
mutable_list.append ("сложная работа")
print (mutable_list)