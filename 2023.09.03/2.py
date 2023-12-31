from utils import important_message

def main() -> None:
    """Функция которая запрашивает у пользователя сообщение и выводит его с помощью функции important_message из другого модуля"""
    print(important_message(input("текст сообщения: ")))
    return None
    
# >>> main()
# текст сообщения: ЗАГОЛОВОК ПРОГРАММЫ
# #========================================================================#
# #                                                                        #
# #                          ЗАГОЛОВОК ПРОГРАММЫ                           #
# #                                                                        #
# #========================================================================#
# >>> text = 'Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы'
# >>> msg = important_message(text)
# >>> print(msg)
# #========================================================================#
# #                                                                        #
# #  Обратите внимание на очень важное сообщение от команды разработчико   #
# #                     в этой великолепной программы                      #
# #                                                                        #
# #========================================================================#
