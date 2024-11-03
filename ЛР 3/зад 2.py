def find_common_participants(group1, group2, separator=","):
 """
 Функция для поиска общих участников в двух группах.

 Args:
  group1: Строка с фамилиями участников первой группы, разделенных separator.
  group2: Строка с фамилиями участников второй группы, разделенных separator.
  separator: Разделитель фамилий в строках. По умолчанию запятая.

 Returns:
  Список общих участников, отсортированный в алфавитном порядке.
 """
 participants1 = set(group1.split(separator))
 participants2 = set(group2.split(separator))
 common_participants = sorted(participants1.intersection(participants2))
 return common_participants

# Пример использования:
group1 = "Иванов,Петров,Сидоров,Кузнецов"
group2 = "Петров,Кузнецов,Смирнов,Васильев"

common_participants = find_common_participants(group1, group2)
print("Общие участники:", common_participants) # Вывод: Общие участники: ['Кузнецов', 'Петров']
