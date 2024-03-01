a = 0
for i in range(0, 1000):
    a = a + i
    if a % 3 == 0 or a % 5 == 0:
        print(a)
