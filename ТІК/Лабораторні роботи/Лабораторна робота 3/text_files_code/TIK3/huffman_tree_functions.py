from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any


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

    def get_huffman_dict(self):
        codes_dict = dict()
        self.__inorder_dfs('', codes_dict, self.root)
        print()

        return codes_dict

    def __inorder_dfs(self, current_code, codes_dict, node):

        if node is None:
            return

        self.__inorder_dfs(current_code + '0', codes_dict, node.left_child)

        if node.value is not None:
            codes_dict[node.value] = current_code
            print(node.value, end=' ')

        self.__inorder_dfs(current_code + '1', codes_dict, node.right_child)

    def get_symbol(self, code):
        return self.__get_symbol(code, self.root)

    def __get_symbol(self, current_code, node):

        if node.value is not None:
            return node.value, current_code

        if len(current_code) == 0:
            raise Exception('Given code does not match any symbol.')

        if current_code[0] == '0':
            return self.__get_symbol(current_code[1:], node.left_child)

        elif current_code[0] == '1':
            return self.__get_symbol(current_code[1:], node.right_child)


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
        print(f'New element: priority - {item1[0] + item2[0]}, nodes - {item1[1], item2[1].value}')
        p_queue.put(result)

    return HuffmanTree(p_queue.get().unpack()[1])


if __name__ == '__main__':
    msg = 'beep boop beer!'
    print(__construct_frequency_list(msg))
    tree = build_huffman_tree(msg)
    print(tree.get_huffman_dict())
    print(tree.get_symbol('111'))


