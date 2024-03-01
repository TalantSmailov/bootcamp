
# ==========================================================                1                     ==============================================================================

# Задание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


a = 0
for i in range(0, 1000):
    a = a + i
    if a % 3 == 0 or a % 5 == 0:
        print(a)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №2:
# a = 333
# b = 555
# Поменяйте значения переменных местами(НЕ ВРУЧНУЮ!), чтобы в ПЕРЕМЕННОЙ "a" было значение 555, а в ПЕРМЕННОЙ "b" было значение 333.

a = 333
b = 555
a = a + b
b = a - b
a = a - b

print('a =', a)
print('b =', b)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.

a = 4729461084
b = 0
while a > 0:
    c = a % 10
    b = b + c
    a = a // 10
print(b)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:

# date = {
# "year": "2020",
# "month": "10",
# .....
# }

datetime = input("Введите дату и время в формате 'гггг-мм-дд чч:мм': ")
date_elements = datetime.split()
date = date_elements[0].split("-")
time = date_elements[1].split(':')
date_dict = {
    "year": date[0],
    "month": date[1],
    "day": date[2],
    "hour": time[0],
    "minute": time[1]
}

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №5:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?
Пропустить

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №6:
# Напишите команду Linux которая создаст ДИРЕКТОРИЮ в НЕСУЩЕСТВУЮЩЕЙ директории БЕЗ ОШИБОК!

mkdir -p /Users/user/Desktop/python_bootcamp


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задание №7:
# Как в Linux выглядит полный путь до Desktop Директории для пользователя 'developer'.

pwd: /Users/user
cd: Desktop
pwd: /Users/user/Desktop



# ===========================================================                2                     ===============================================================================



# Задача 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые больше 5.
 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i > 5:
        print(i)
 
 
#Задача 2
# Есть набор чисел 
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# Поделить каждое число из digits на 9 и вывести на экран.

digits = (113, 118, -5, 1, 135, 137, 0, 142, 144, 17, 154, 0, 155, 2, 159, 172)
for i in digits:
    print(i / 9)


# Задача 3
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
for i in spisok_2:
    if i not in spisok_1:
        print(i)




# ========================================================                3                     ===============================================================================


# Задание 1:
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов
#    и останавливается, если встречает число 237.

for i in range(300):
    if i % 2 == 0:
        print(i)
    if i == 237:
        break


# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
    # Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно короче 6 символов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна быть на один жлемент больше)
# 3. Переставьте эти две части местами и запишите в лист. 

while True:
    sentence = input("Введите предложение: ")
    words = sentence.split()
    if len(words) < 6:
        print("Попробуйте еще раз.")
    else:
        break

middle_index = len(words) // 2
if len(words) % 2 == 0:
    first_half = words[:middle_index]
    second_half = words[middle_index:]
else:
    first_half = words[:middle_index + 1]
    second_half = words[middle_index + 1:]

new_sentence = second_half + first_half

print(new_sentence)


# Задание 3:
# Вам дан список:
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# Определите количество четных и не четных.

numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Четные:", even_count)
print("Нечетные:", odd_count)

# Задание 4:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.

numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
new_numbers = [-1 if num < 0 else 1 if num > 0 else 0 for num in numbers]

print(new_numbers)


# Задание 5:
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# Выведите все элементы списка с четными ИНДЕКСАМИ (то есть A[0], A[2], A[4], ... ])

my_list = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11, 13, 17]
for i in my_list:
    if my_list.index(i) % 2 == 0:
        print(i)



# Задание 6:
# Дан список чисел:
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# Выведите все элементы списка, которые больше предущего элемента
# Пример: (numbers: 1,5,2,4,3 Результат: 5,4)







# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет, 
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно






################################################################################



# Задание 2:
    # Даны три переменные "A", "B" и "C". 
    # Изменить значения этих переменных так, чтобы в "A" хранилось значение "A"+"B", 
    # в "B" хранилась разность старых значений "C" - "A", 
    # а в "C" хранилось сумма старых значений "A" + "B" + "C". 
    # Например, A=0, B=2, C=5, тогда новые значения A=2, B=5 и C=7.



################################################################################



# Задание 3:
    # Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.


################################################################################



# Задание 4:
    # Вам даны несколько последовательностей чисел:
    # sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
    # sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
    # sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
    # sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

    # Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
    # Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
    # Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
    # Если в решении задания не присутствует цикл ---> Задание не защитано.



################################################################################



# Задание 5:
    # Создайте input и спросите у пользоваетля как работает встроенная функция reversed().
    # В терминале пользователя должен ввести пример функции reversed() и отправить это вашей программе.
    # Ваша программа должна исполнить ту часть кода которую ввёл пользователь и вывести на экран результат.
    # Если пользователь ввёл что-то не по синтаксису Python поймайте это с помощью try: except:
    # Если пользователь всё ввёл верно выполните его программу.
    # Если поймали ошибку ---> Спросите снова как работает встроенная функция reversed().




################################################################################



# Задание 6:
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию? 
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.


#################################################################################

