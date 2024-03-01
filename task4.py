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
