salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
spend_month = spend
for i in range (months):
    if i > 0 :
        spend_month = spend_month + spend_month * increase
    money_capital = money_capital + (spend_month - salary)
end_money = round(money_capital)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", end_money)