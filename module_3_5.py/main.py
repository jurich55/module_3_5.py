def get_multiplied_digits(number):
    str_number = str(number)             # Строковое представление(str) числа number
    first = int(str_number[0])           # Выделили первый элемент строки  str(number)
    if (len(str_number[1:])) <= 1:       # проверка условия "длина str_number не больше 1"
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)


# Тренировка
#def fact_(n):  # вычисление факториала числа n
#    if n <= 1:
#        return 1
#    else:
#        return n * fact_(n - 1)


#a = fact_(5)
#print(a)
