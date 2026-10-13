a = float(input("Число 1: "))
b = float(input("Число 2: "))
c = float(input("Число 3: "))

total = a + b + c
average = total / 3

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print("Сумма:", total)
print("Среднее:", average)
print("Максимум:", maximum)