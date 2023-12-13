from decimal import Decimal
from datetime import time, date, datetime
from numbers import Number

class PowerMeter:
    """класс который описывает двухтарифный счётчик потреблённой электрической мощности."""
    
    def __init__(self):
        """констркутор"""
        self.tariff1: Number = 8.00 # первый тариф (ночной трафик);
        self.tariff2: Number = 6.50 # второй тариф (дневной трафик);
        self.tariff2_starts: time = time(6) # время начала действия второго тарифа;
        self.tariff2_ends: time = time(18) # время окончания действия второго тарифа;
        self.power: Decimal # суммарная потреблённая мощность;
        self.charges: dict[date, float] = dict() # запись по месецам потребление электроэнергии;

    def meter(self, power_: Number) -> Decimal:
        """принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент"""

        new_time = datetime.now() # Вычисление текущей даты и времени;
        self.power = Decimal(round(Decimal(power_), 1)) # суммарная потреблённая мощность в данный месяц;
        charge = 0 # стоимость потребления электроэнергии;
        
        if self.tariff2_starts.hour < new_time.time().hour < self.tariff2_ends.hour:
            charge = round(Decimal(power_ * self.tariff2), 2) # вычисление стоимости потребления электроэнергии в дневное время;
        else:
            charge = round(Decimal(power_ * self.tariff1), 2) # вычисление стоимости потребления электроэнергии в ночное время;

        new_date = date.today().month # текущая дата;

        self.charges[new_date] = charge # Запись стоимости потребления электроэнергии в текущий месяц;

        return Decimal(charge)
    
    def __repr__(self):
        # машиночитаемое строковое представление;
        return f'<{type(self).__name__}: {self.power}кВт/ч>'
    
    def __str__(self):
        # человекочитаемое строковое представление;
        data = list((f'({datetime(2023, k, 1).strftime("%B")[:3]}) {v}' for k, v in self.charges.items()))
        return '/n'.join(data)
    
# >>> pm1 = PowerMeter()
# >>>
# >>> pm1.meter(2)
# Decimal('16.00')
# >>> pm1.meter(1.2)
# Decimal('9.60')
# >>>
# >>> pm1
# <PowerMeter: 1.2кВт/ч>
# >>> print(pm1)
# (Dec) 9.60