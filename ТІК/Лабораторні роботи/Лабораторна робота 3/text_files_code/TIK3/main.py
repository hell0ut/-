import huffman_tree_functions


def huffman_encode(huffman_dict, message):
    result = ''
    for symbol in message:
        # TODO: sent some stuff to a buffer when encoding files
        result += huffman_dict[symbol]

    return result


def huffman_decode(huffman_tree, encoded_message):
    result = ''
    while len(encoded_message) > 0:
        symbol, remaining_message = huffman_tree.get_symbol(encoded_message)
        result += symbol
        encoded_message = remaining_message

    return result


if __name__ == '__main__':
    msg = 'насікан дмитро юрійович 22.10.2001 заставна'
    tree = huffman_tree_functions.build_huffman_tree(msg)
    huffman_dict = tree.get_huffman_dict()

    enc_msg = huffman_encode(huffman_dict, msg)
    dec_msg = huffman_decode(tree, enc_msg)

    print(huffman_dict)
    print(f'Original message: {msg}.\nEncoded message: {enc_msg}.\nDecoded message: {dec_msg}')
