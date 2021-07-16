import math


def main_analyzer(message):
    symbols = dict()

    # рахуємо кількість символів у алфавіті та входження кожного символа
    for sym in message:
        symbols[sym] = symbols.get(sym, 0) + 1

    # обчислюємо ентропію та кількість інформації
    size = len(message)
    entropy = 0
    for num in symbols.values():
        probability = num / size
        entropy += probability * math.log2(probability)

    entropy = -entropy
    information_amount = size * math.log2(len(symbols.keys()))

    print(f'Довжина тексту - {size}')
    print(f'Ентропія тексту - {entropy}')
    print(f'Кількість інформації тексту - {information_amount}')


MODE = int(input('Виберіть режим роботи:\n1 - текстовий файл\n2 - введення повідомлення вручну\n\n'))

if MODE == 1:
    file_name = input('Уведіть назву файлу без розширення: ') + '.txt'

    # читаємо дані з файлу
    with open(file_name, 'r', encoding='utf-8') as file:
        text_message = file.read()
        print(text_message)
    main_analyzer(text_message)

elif MODE == 2:
    text_message = input('Введіть ваше текстове повідомлення: ')
    main_analyzer(text_message)


