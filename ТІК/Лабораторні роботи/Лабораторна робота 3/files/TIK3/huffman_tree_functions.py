from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any
from bitarray import bitarray


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

    def unpack(self):
        return self.priority, self.item

    @staticmethod
    def pack(unpacked_item):
        return PrioritizedItem(unpacked_item[0], unpacked_item[1])


class TreeNode:

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class HuffmanTree:

    def __init__(self, root):
        self.root = root
        self.current_node = self.root
        self.serialized_tree_path = bitarray()

    def get_huffman_dict(self):
        codes_dict = dict()
        self.__inorder_dfs('', codes_dict, self.root)

        return codes_dict

    # обходимо дерево для отримання таблиці елемент: код
    def __inorder_dfs(self, current_code, codes_dict, node):

        if node is None:
            return

        self.__inorder_dfs(current_code + '0', codes_dict, node.left_child)

        if node.value is not None:
            codes_dict[node.value] = current_code

        self.__inorder_dfs(current_code + '1', codes_dict, node.right_child)

    # побітово рухаємося по дереву (0 - вліво, 1 - вправо), поки не буде знайдений листок
    def feed_bit(self, bit):

        if bit == 0:
            self.current_node = self.current_node.left_child

        if bit == 1:
            self.current_node = self.current_node.right_child

        if self.current_node.value is not None:
            val = self.current_node.value
            self.current_node = self.root

            return val

    # старий метод, використовувати тільки для текстових кодів
    def get_symbol(self, code):
        return self.__get_symbol(code, self.root)

    # старий метод, використовувати тільки для текстових кодів
    def __get_symbol(self, current_code, node):

        if node.value is not None:
            return node.value, current_code

        if len(current_code) == 0:
            raise Exception('Given code does not match any symbol.')

        if current_code[0] == '0':
            return self.__get_symbol(current_code[1:], node.left_child)

        elif current_code[0] == '1':
            return self.__get_symbol(current_code[1:], node.right_child)

    # отримуємо бітове представлення дерева у форматі 1 - звичайний вузол, 0 - листок + значення листка у бітах
    def get_path(self):
        self.__get_path(self.root)
        return self.serialized_tree_path

    def __get_path(self, node):

        if node.value is not None:
            value_bits = bitarray()
            value_bits.frombytes(node.value.to_bytes(1, 'little'))
            value_bits.insert(0, 0)
            self.serialized_tree_path += value_bits

        else:
            self.serialized_tree_path.append(1)

            self.__get_path(node.left_child)
            self.__get_path(node.right_child)


# отримуємо список унікальних символів з файлу та кількість входжень кожного з них
def __construct_frequency_list(message):
    result = {}
    list_result = []

    for symbol in message:
        try:
            info = result[symbol]
        except KeyError:
            info = 0
        info += 1
        result[symbol] = info

    for key, value in result.items():
        list_result.append([key, value])

    return sorted(list_result, key=lambda x: x[1], reverse=True)


def __construct_priority_queue(frequency_list):
    queue = PriorityQueue()

    for symbol in frequency_list:
        queue.put(PrioritizedItem(symbol[1], TreeNode(symbol[0])))

    return queue


def build_huffman_tree(message):
    p_queue = __construct_priority_queue(__construct_frequency_list(message))

    while p_queue.qsize() > 1:
        item1 = p_queue.get().unpack()
        item2 = p_queue.get().unpack()

        result = PrioritizedItem.pack((item1[0] + item2[0], TreeNode(None, left_child=item1[1], right_child=item2[1])))
        p_queue.put(result)

    return HuffmanTree(p_queue.get().unpack()[1])


class HuffmanBuilder:

    def __init__(self, path):
        self.path = path

    def get_next_path_item(self):
        next_item = self.path[0]
        self.path = self.path[1:]
        return next_item

    def get_leaf_value(self):
        value = self.path[0:8]
        self.path = self.path[8:]
        return value

    def build_tree(self):
        return HuffmanTree(self.__build_tree_from_path())

    def __build_tree_from_path(self):

        current_path_item = self.get_next_path_item()

        if current_path_item == 1:
            current_node = TreeNode(None)
            current_node.left_child = self.__build_tree_from_path()
            current_node.right_child = self.__build_tree_from_path()

        else:
            current_node = TreeNode(int.from_bytes(self.get_leaf_value().tobytes(), 'little'))

        return current_node

