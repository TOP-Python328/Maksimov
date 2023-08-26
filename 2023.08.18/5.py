def central_tendency(number_one: int, number_two: int, *numbers: int) -> dict[str, float]:

    work_numbers = [number_one, number_two, *numbers]
    central_tendency_result = {'median': float,
                               'arithmetic': float,
                               'geometric': float,
                               'harmonic': float,
                               }
    # расчет медианы;
    if len(work_numbers) % 2 == 0:
        central_tendency_result['median'] = (work_numbers[int(len(work_numbers) / 2)] + work_numbers[int((len(work_numbers) / 2) - 1)]) / 2
    else:
        central_tendency_result['median'] = float(work_numbers[len(work_numbers) // 2])
    
    # расчет среднюю арифметическую;
    central_tendency_result['arithmetic'] = sum(n for n in work_numbers) / len(work_numbers);
    
    # расчет среднюю геометрическую;
    res_multip_ = 1
    for n in work_numbers:
        res_multip_ = res_multip_ * n
    central_tendency_result['geometric'] = res_multip_ ** (1 / len(work_numbers))
    
    # расчет среднюю гармоническую;
    central_tendency_result['harmonic'] = len(work_numbers) / sum(1 / n for n in work_numbers);
    
    return central_tendency_result
   
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

# >>> central_tendency(1)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: central_tendency() missing 1 required positional argument: 'number_two'

# >>> central_tendency(1, 2)
# {'median': 1.5, 'arithmetic': 1.5, 'geometric': 1.4142135623730951, 'harmonic': 1.3333333333333333}
