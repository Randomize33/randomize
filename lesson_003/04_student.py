# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
total_expenses=0
i=0
while i<10:
    total_expenses += expenses
    expenses = expenses * 1.03
    i+=1

total_educational_grant=educational_grant*10
money_from_parent=round(total_expenses - total_educational_grant,2)
print ('Студенту надо попросить ' + str(money_from_parent) + 'рублей')

