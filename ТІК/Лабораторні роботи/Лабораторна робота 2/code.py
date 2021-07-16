# повертає відсортований список з частотою зустрічі кожного символа
def construct_frequency_list(message):
    result = {}
    list_result = []

    for symbol in message:
        try:
            info = result[symbol]
        except KeyError:
            info = 0
        info += 1
        result[symbol] = info

    for symbol in result.keys():
        info = result[symbol]
        info = [info, round(info / len(message), 3)]
        list_result.append([symbol, info])

    return sorted(list_result, key=lambda x: x[1][1], reverse=True)


# обчислює суму починаючи з вибраного символа у вказану сторону
def frequency_sum(frequency_list, start, upper_direction):
    result = 0

    if upper_direction is True:
        while start >= 0:
            result += frequency_list[start][1][1]
            start -= 1

    else:
        while start < len(frequency_list):
            result += frequency_list[start][1][1]
            start += 1

    return round(result, 3)


# знаходить серединний елемент (той, при якому суми рівні)
def find_mid(frequency_list):
    best_result_index = None
    delta = 400000

    for index, item in enumerate(frequency_list):
        upper_sum = frequency_sum(frequency_list, index, True)
        lower_sum = frequency_sum(frequency_list, index + 1, False)

        if delta > abs(upper_sum - lower_sum):
            best_result_index = index
            delta = abs(upper_sum - lower_sum)

    return best_result_index


def shannon_fano_code_constructor(frequency_list):
    result_list = [''] * 256
    __shannon_fano_code_constructor(frequency_list, result_list)
    return result_list


def __shannon_fano_code_constructor(frequency_list, codes_list):
    mid = find_mid(frequency_list)

    upper_part = frequency_list[:mid + 1]
    lower_part = frequency_list[mid + 1:]

    for item in upper_part:
        codes_list[item[0]] += '1'

    for item in lower_part:
        codes_list[item[0]] += '0'

    if len(upper_part) <= 1 and len(lower_part) <= 1:
        return

    if len(lower_part) <= 1:
        __shannon_fano_code_constructor(upper_part, codes_list)
        return

    if len(upper_part) <= 1:
        __shannon_fano_code_constructor(lower_part, codes_list)
        return

    __shannon_fano_code_constructor(upper_part, codes_list)
    __shannon_fano_code_constructor(lower_part, codes_list)


def shannon_fano_encode(message):
    f_list = construct_frequency_list(message)
    codes_list = shannon_fano_code_constructor(f_list)

    encoded_message = ''
    for byte in message:
        encoded_message += codes_list[byte]

    return encoded_message, codes_list


def shannon_fano_decode(codes_dict, name, ext):
    with open(f'{name}.lab1', 'rb') as f:
        decoded_bytes = f.read()
        print('bytes from file:', decoded_bytes)

    encoded_message = ''
    for index, byte in enumerate(decoded_bytes):
        new_byte = f'{byte:b}'
        if len(new_byte) < 8:
            new_byte = '0' * (8 - len(new_byte)) + new_byte
            if index == len(decoded_bytes) - 1:
                new_byte = f'{byte:b}'

        encoded_message += new_byte

    with open(f'{name}-decoded.{ext}', 'wb') as f:
        buffer = ''
        decoded_message = ''
        for symbol in encoded_message:
            buffer += symbol

            try:
                decoded_symbol = codes_dict[buffer]
            except KeyError:
                continue

            f.write(decoded_symbol.to_bytes(1, 'little'))
            buffer = ''
    return decoded_message, encoded_message


def average_code_length(sym_to_code_dict):
    result = 0
    for code in sym_to_code_dict.values():
        result += len(code)

    return result / len(sym_to_code_dict.values())


def write_file(encoded_message, name):
    bytes_array = []

    bytes_s = b''
    while len(encoded_message) > 0:
        bytes_array.append(int(encoded_message[0:8], 2))

        encoded_message = encoded_message[8:]

    print('bytes to file:', end=' ')
    with open(f'{name}.lab1', 'wb') as f:
        for i in bytes_array:
            f.write(i.to_bytes(1, 'little'))
            print(i.to_bytes(1, 'little'), end='')
            bytes_s += i.to_bytes(1, 'little')


if __name__ == '__main__':
    file_name = input('Уведіть назву файлу з розширенням: ')
    with open(file_name, 'rb') as file:
        text_message = file.read()
    print(text_message)
    message, code_list = shannon_fano_encode(text_message)

    print(message)
    print(f'Довжина файлу - {len(text_message)}')

    write_file(message, file_name.split('.')[0])
    print()
    sym_to_code_dict = {byte: index for index, byte in enumerate(code_list)}
    message1, encoded_message = shannon_fano_decode(sym_to_code_dict, file_name.split('.')[0], file_name.split('.')[1])

