numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс None
none_index = numbers.index(None)

# Считаем сумму всех элементов кроме None
sum_numbers = sum(numbers[:none_index] + numbers[none_index + 1:])
# Считаем количество элементов, включая пропуск
count_numbers = len(numbers)

# Вычисляем среднее арифметическое
average = sum_numbers / count_numbers

# Заменяем None на среднее арифметическое
numbers[none_index] = average

print("Измененный список:", numbers)