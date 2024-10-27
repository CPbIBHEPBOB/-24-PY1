salary = 50000  # Ежемесячная зарплата
spend = 60000  # Ежемесячные расходы
increase = 0.05  # Ежемесячный рост цен
target_months = 10  # Целевое количество месяцев

money_capital = 18783  # Начальная подушка безопасности

months = 10  # Счетчик месяцев
current_spend = spend  # Текущие расходы

while months < target_months:
    months += 1
    current_budget = salary - current_spend  # Бюджет текущего месяца
    if current_budget < 18783:
        money_capital -= abs(current_budget)  # Изменение подушки безопасности
    current_spend *= (1 + increase)  # Увеличение расходов с учетом роста цен

print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов: {round(money_capital)}")

