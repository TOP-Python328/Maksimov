Number_int = input('введите целое число (в милях) ')
Number_float = input('введите дробное число (в милях) ')
miles = float(Number_int + "." + Number_float)
kilometers = f'{(miles * 1.61):.1f}'
print(miles, ' миль = ', kilometers, ' км')

#введите целое число (в милях) 15
#введите дробное число (в милях) 7
#15.7  миль =  25.3  км