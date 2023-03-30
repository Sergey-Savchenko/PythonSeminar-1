# Найдите сумму цифр трехзначного числа.

# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

numb = int(input('Введите трёхзначное число: '))
first = numb%10
# print(first)
second = numb%100//10
# print(second)
third = numb//100
# print(third)
sum = first+second+third
print(f"Сумма цифр трехзначного числа: {sum}")
fsum = numb%10 + numb%100//10 + numb//100
print(fsum)