money_capital = 150000  # Финансовая подушка безопасности
salary = 50000  # Ежемесячная зарплата
spend = 60000  # Ежемесячные расходы
increase = 0.05  # Ежемесячный рост цен

months = 1  # Счетчик месяцев
current_budget = money_capital + salary  # Бюджет первого месяца
current_spend = spend  # Текущие расходы

while current_budget >= current_spend:
    months += 1
    current_budget -= current_spend  # Изменение бюджета после расходов
    current_spend *= (1 + increase)  # Увеличение расходов с учетом роста цен
    current_budget += salary  # Добавление зарплаты в бюджет

print("Количество месяцев, которое можно протянуть без долгов:", months, )

