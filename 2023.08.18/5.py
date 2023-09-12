def central_tendency(number_one: float, number_two: float, *numbers_: float) -> dict[str, float]:
    """Функция вычисляет основные меры центральной тенденции для некоторого количества чисел"""
    numbers = [number_one, number_two, *numbers_]
    central_tendency_result = {'median': float,
                               'arithmetic': float,
                               'geometric': float,
                               'harmonic': float,
                               }
    # расчет медианы;
    numbers = sorted(numbers, reverse=True)
    if len(numbers) % 2 == 0:
        num_s = len(numbers) / 2
        central_tendency_result['median'] = (numbers[int(num_s)] + numbers[int((num_s) - 1)]) / 2
    else:
        central_tendency_result['median'] = float(numbers[len(numbers) // 2])
    # расчет среднюю арифметическую;
    central_tendency_result['arithmetic'] = sum(n for n in numbers) / len(numbers)
    # расчет среднюю геометрическую;
    res_multip_ = 1
    for n in numbers:
        res_multip_ = res_multip_ * n
    central_tendency_result['geometric'] = res_multip_ ** (1 / len(numbers))
    # расчет среднюю гармоническую;
    try:
        central_tendency_result['harmonic'] = len(numbers) / sum(1 / n for n in numbers if not n == 0)
    except:
        central_tendency_result['harmonic'] = 0
    return central_tendency_result


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>
# >>> central_tendency(1)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: central_tendency() missing 1 required positional argument: 'number_two'
# >>>
# >>> central_tendency(1, 2)
# {'median': 1.5, 'arithmetic': 1.5, 'geometric': 1.4142135623730951, 'harmonic': 1.3333333333333333}
# >>>
# >>> central_tendency(2, 5, 1, 4, 3)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>
# >>> central_tendency(1, 0, -1)
# {'median': 0.0, 'arithmetic': 0.0, 'geometric': 0.0, 'harmonic': 0}
