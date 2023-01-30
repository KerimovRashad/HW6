number = int(input("Введите число: "))
lst = []
for i in range(number):
    lst.append((-3)**i)
print(f"Итоговая последовательность: {lst}")
# улучшение

lst = [(-3)**i for i in range(number)]
print(f"Итоговая последовательность после применения list comprehension: {lst}")