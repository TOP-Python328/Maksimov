list_of_dicts = [
    {
        'Барнаул': 4,
        'Владивосток': 3,
        'Волгоград': 2,
        'Нижний Новгород': 8,
        'Санкт-Петербург': 4,
        'Ульяновск': 8,
        'Уфа': 7,
        'Хабаровск': 2,
        'Ярославль': 1
    },
    {
        'Владивосток': 3,
        'Воронеж': 4,
        'Казань': 2,
        'Москва': 8,
        'Новокузнецк': 3,
        'Новосибирск': 4,
        'Омск': 1,
        'Пермь': 2,
        'Тольятти': 1,
        'Уфа': 3
    },
    {
        'Барнаул': 1,
        'Владивосток': 1,
        'Волгоград': 9,
        'Москва': 1,
        'Новосибирск': 6,
        'Санкт-Петербург': 3,
        'Ульяновск': 9
    },
    {
        'Владивосток': 1,
        'Воронеж': 3,
        'Екатеринбург': 6,
        'Оренбург': 3,
        'Санкт-Петербург': 8,
        'Тольятти': 2
    }
]

cities_set = set()
for i in range(len(list_of_dicts)):
    cities_set = cities_set | set(list_of_dicts[i])
# ИСПОЛЬЗОВАТЬ: генераторное выражение
cities_set = {city for cities_dict in list_of_dicts for city in cities_dict}

# ИСПРАВИТЬ: функция sorted() сортирует элементы переданного итерируемого объекта по возрастанию — reverse=False можно опустить
cities_values = dict.fromkeys(sorted(cities_set, reverse=False), set())

for cities_dict in list_of_dicts:
    for city, val in cities_values.items():
        # ИСПРАВИТЬ: использование словарных методов get() и setdefault() позволяет избежать явного перехвата исключений
        try:
            # ИСПРАВИТЬ: на предложенном наборе данных эта проверка всегда вернёт True, следовательно в ней нет смысла
            # КОММЕНТАРИЙ: перехват исключения может выполняться и без проверки, в любом выражении
            if cities_dict[city]:
                try:
                    cities_values[city] = cities_values[city] | {str(cities_dict[city])}
                except KeyError:
                    # УДАЛИТЬ: данное выражение не используется
                    cities_values[city]
        except KeyError:
            # УДАЛИТЬ: данное выражение не используется
            cities_values[city]

for k, v in cities_values.items():
    print(f'{k}: {v}')


# Барнаул: {'1', '4'}
# Владивосток: {'3', '1'}
# Волгоград: {'2', '9'}
# Воронеж: {'3', '4'}
# Екатеринбург: {'6'}
# Казань: {'2'}
# Москва: {'8', '1'}
# Нижний Новгород: {'8'}
# Новокузнецк: {'3'}
# Новосибирск: {'6', '4'}
# Омск: {'1'}
# Оренбург: {'3'}
# Пермь: {'2'}
# Санкт-Петербург: {'8', '3', '4'}
# Тольятти: {'1', '2'}
# Ульяновск: {'8', '9'}
# Уфа: {'3', '7'}
# Хабаровск: {'2'}
# Ярославль: {'1'}


# ИТОГ: хорошо, но можно лучше — 3/5


# ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует добавлять пробелы вокруг = при передаче аргументов по ключу
# КОММЕНТАРИЙ: когда аргумент передаётся в функцию с указанием параметра, например print(end='\n\n'), то это называется передачей аргумента по ключу — пробелы вокруг символа '=' в таком случае на ставятся
