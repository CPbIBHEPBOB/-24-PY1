# Параметры
diskette_capacity = 1.44 * 1024 * 1024 # Емкость дискеты в байтах
pages_per_book = 100 # Количество страниц в книге
rows_per_page = 50 # Число строк на странице
symbols_per_row = 25 # Количество символов в строке
bytes_per_symbol = 4 # Количество байт на символ

# Вычисляем размер книги в байтах
book_size = pages_per_book * rows_per_page * symbols_per_row * bytes_per_symbol

# Вычисляем количество книг
number_of_books = diskette_capacity // book_size

print("Количество книг, помещающихся на дискету:", int(number_of_books)) # Преобразуем в целое число