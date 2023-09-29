from datetime import date, timedelta
from itertools import count

# Шаблон исключаемого периода
vacations = [
    (date(1800, 1, 1), timedelta(weeks=1)),
    (date(1800, 1, 1), timedelta(weeks=1))
]

def schedule(starting_date: 'date', first_lesson: int, second_lesson: int, total_days: int) -> list['data']:
    """Функция которая генерирует график проведения мероприятий по заданным условиям"""

    list_of_classes = list() # список занятий
    days_of_exclusion = list() # список исключенных дней
    
    # цикл для определения списка исключенных дней
    for weeks in vacations:
        for day in range(weeks[1].days):
            day_exc = weeks[0] + timedelta(day)
            days_of_exclusion.append(day_exc)
    
    days_num = count(0, 7) # бесконечный недельный период
    difference = timedelta(second_lesson - first_lesson) # разница между занятиями в неделе
   
    # цикл для определение даты занятий
    for day in days_num:
        day = starting_date + timedelta(day)
        if day not in days_of_exclusion:
            list_of_classes.append(day.strftime('%d/%m/%Y'))
        day = (day + difference)
        if day not in days_of_exclusion:
            list_of_classes.append(day.strftime('%d/%m/%Y'))
        if len(list_of_classes) == total_days:
            break
    
    return list_of_classes
    
    
# >>> vacations = [
# ...     (date(2023, 5, 1), timedelta(weeks=1)),
# ...     (date(2023, 7, 17), timedelta(weeks=1)),
# ... ]
# >>>
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
# >>>
# >>> len(py321)
# 70
# >>> py321[28:32]
# ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']