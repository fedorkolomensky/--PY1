salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

delta = salary - spend
while months > 0:
    spend = spend * (1 + increase)
    need_money -= delta
    delta = salary - spend
    months -= 1

print(round(need_money))