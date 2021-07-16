import huffman_tree_functions
import math
from bitarray import bitarray


def huffman_encode(huffman_dict, message):
    result = bitarray()
    for symbol in message:
        result += bitarray(huffman_dict[symbol])

    return result


def huffman_decode(huffman_tree, encoded_message, file_name):
    with open(f'{file_name.split("-")[0]}-decoded.{file_name.split("-")[1]}', 'wb') as f:

        for index, bit in enumerate(encoded_message):
            try:
                f.write(huffman_tree.feed_bit(bit).to_bytes(1, 'little'))
            except AttributeError:
                continue


def calculate_entropy(frequency_list, size):
    i = 0
    entropy = 0
    while i < len(frequency_list):
        probability = frequency_list[i][1] / size
        entropy += probability * math.log2(probability)
        i += 1
    return -entropy


def encode_file(file_name, extension):
    with open(f'{file_name}.{extension}', 'rb') as file:
        bytes_from_file = file.read()

    # будуємо дерево Хаффмана
    huff_tree = huffman_tree_functions.build_huffman_tree(bytes_from_file)
    # отримуємо таблицю Хаффмана
    huff_dict = huff_tree.get_huffman_dict()

    # кодуємо послідовність байтів з файлу
    enc_bytes = huffman_encode(huff_dict, bytes_from_file)
    # перетворюємо дерево у bitarray
    encoded_tree = huff_tree.get_path()

    # доповнюємо bitarray нулями до тих пір, поки його довжина не ділиться на 8
    encoded_tree.fill()

    # отримуємо довжину дерева у байтах
    tree_len_bytes = len(encoded_tree).to_bytes(2, 'little')

    # записуємо дані у файл
    with open(f'{file_name}-{extension}-encoded.lab3', 'wb') as file:
        file.write(tree_len_bytes)
        encoded_tree.tofile(file)
        enc_bytes.tofile(file)


def decode_file(file_name):
    tree_path = bitarray()
    encoded_bytes_from_file = bitarray()

    with open(f'{file_name}.lab3', 'rb') as file:
        # читаємо довжину дерева у бітах
        tree_len = file.read(2)
        tree_len = int.from_bytes(tree_len, 'little')

        # читаємо байти дерева з файлу
        raw_tree_bytes = file.read(int(tree_len / 8))
        tree_path.frombytes(raw_tree_bytes)

        # будуємо дерево Хаффмана з його бітового представлення
        tree_builder = huffman_tree_functions.HuffmanBuilder(tree_path)
        tree_from_file = tree_builder.build_tree()

        # читаємо закодований вміст файлу
        encoded_bytes_from_file.frombytes(file.read())

    # розкодовуємо вміст файлу та записуємо результат у файл
    huffman_decode(tree_from_file, encoded_bytes_from_file, file_name)


if __name__ == '__main__':
    while True:
        print('\n[1] [Закодувати файл]\n[2] [Розкодувати файл]\n[3] [Знайти ентопію файлу]\n[4] [Вийти]\n')
        option = input('Уведіть цифру для вибору опції: ')

        if option == '1':
            f_n = input('Уведіть назву файлу: ')
            ext = input('Уведіть розширення: ')

            encode_file(f_n, ext)

        elif option == '2':
            f_n = input('Уведіть назву файлу: ')
            decode_file(f_n)

        elif option == '3':
            f_n = input('Уведіть назву файлу: ')
            ext = input('Уведіть розширення: ')
            with open(f'{f_n}.{ext}', 'rb') as file:
                contents = file.read()

            f_list = huffman_tree_functions.__construct_frequency_list(contents)

            print(calculate_entropy(f_list, len(contents)))

        elif option == '4':
            break
