text = input('Введите предложение: ')
punctuation = '.,:;!?–—\'\"()*/'

# ОТВЕТИТЬ: какова цель преобразования в списки?
text = list(text)
punctuation = list(punctuation)

text_exit = ''
# ИСПРАВИТЬ: согласно условию задачи вам необходимо было использовать генераторное выражение
for t in text:
    check = 'нет'
    for s in punctuation:
        if t == s:
            check = 'да'
    if check == 'нет':
        text_exit = text_exit + t

print(text_exit)


# Введите предложение: Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.
# Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита


# ИТОГ: переделать — 0/3
