# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
#[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

s = 0
n = [2, 3, 5, 9, 3]
for i in range(len(n)):
    if i % 2 != 0:
        s += n[i]
print(s)