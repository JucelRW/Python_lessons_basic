# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit = ["Банан", "Апельсин", "Мандарин", "Груша", "Слива"]
last_name = len(fruit)
for i in range(last_name):
    print(str(i+1) + '.' + '{}'.format(fruit[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

one_list = [1, 3, 5, 7, 8, 10]
two_list = [1, 3, 8, 10, 11, 12]
for item in two_list:
    if item in one_list:
     one_list.remove(item)
print(one_list)
print(two_list)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

first_list = [2, 13, 23, 27, 22, 36]
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
      new_list.append(first_list[i] / 4)
    else:
      new_list.append(first_list[i] * 2)
    print(new_list)