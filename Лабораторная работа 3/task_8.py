money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

ostatok = money_capital + salary - spend
while (ostatok) > 0:
     spend = spend * (1 + increase)
     ostatok += salary - spend
     month += 1

print(month)