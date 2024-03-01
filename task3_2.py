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

