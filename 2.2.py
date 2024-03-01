# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
    # Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно короче 6 слов, спрашивайте снова и снова.
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