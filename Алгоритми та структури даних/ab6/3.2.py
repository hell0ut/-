class Node:
    def __init__(self, capacity, value=None):
        self.next = [None] * capacity
        self.num_of_letters = 0
        self.last = None
        self.value = value


class Trie:
    letter_capacity = 26

    def __init__(self):
        self.root = Node(Trie.letter_capacity)

    @staticmethod
    def get_index(letter):
        return ord(letter) - ord("a")

    @staticmethod
    def get_letter(index):
        return chr(index + ord("a"))

    def put(self, word):
        self.recursive_put(self.root, word, 0)

    def recursive_put(self, current_node, word, step):
        if current_node is None:
            current_node = Node(Trie.letter_capacity)
        if step == len(word):
            current_node.value = True
            return current_node
        index = ord(word[step]) - ord("a")
        if current_node.next[index] is None:
            current_node.num_of_letters += 1
            current_node.last = index
        current_node.next[index] = self.recursive_put(current_node.next[index], word, step + 1)
        return current_node

    def recursive_find(self, word, step, current_node):
        if current_node is None:
            return None
        if step == len(word) - 1:
            return current_node.value
        i = self.get_index(word[step])
        return self.recursive_find(word, step + 1, current_node.next[i])

    def find(self, word):
        return self.recursive_find(word, 0, self.root)

    def get_tree_pic(self, current_node=None, symbol=None):
        if current_node is None:
            current_node = self.root
        if symbol is None:
            symbol = "*"

        if current_node.num_of_letters == 0:
            return [symbol]
        elif current_node.num_of_letters == 1:
            pictures = self.get_tree_pic(current_node.next[current_node.last], self.get_letter(current_node.last))
            i = 0
            while i < len(pictures):
                if pictures[i][0] != ' ':
                    pictures[i] = symbol + '\u2500'*3 + pictures[i]
                else:
                    pictures[i] = ' '*4 + pictures[i]
                i += 1
            return pictures
        else:
            tree_pic = []
            num_of_letters = 0
            for i in range(len(current_node.next)-1, -1, -1):
                if current_node.next[i] is not None:
                    num_of_letters += 1
                    child_tree = self.get_tree_pic(current_node.next[i], self.get_letter(i))
                    tree_pic.extend(child_tree)
                    tree_pic.append(' ')
            tree_pic = tree_pic[:-1]
            return self.merge_pics(tree_pic, num_of_letters, symbol)

    @staticmethod
    def merge_pics(graphic_tree, num_of_letters, symbol):
        flag = True
        counter = 0
        for i in range(len(graphic_tree)):

            if graphic_tree[i][0] == " ":
                if flag:
                    graphic_tree[i] = " " * 4 + graphic_tree[i]
                else:
                    graphic_tree[i] = "  \u2502 " + graphic_tree[i]
            else:
                if counter == 0:
                    graphic_tree[i] = "  \u250c\u2500" + graphic_tree[i]
                    flag = False
                elif counter == num_of_letters - 1:
                    graphic_tree[i] = "  \u2514\u2500" + graphic_tree[i]
                    flag = True
                else:
                    graphic_tree[i] = "  \u251c\u2500" + graphic_tree[i]
                counter += 1
        index = len(graphic_tree) // 2
        if graphic_tree[index][2] == "\u251c":
            graphic_tree[index] = symbol + "\u2500\u253c" + graphic_tree[index][3:]
        else:
            graphic_tree[index] = symbol + "\u2500\u2524" + graphic_tree[index][3:]
        return graphic_tree

    def print_trie(self):
        result_arr = self.get_tree_pic()
        result = ""
        for piece in result_arr:
            result += piece + "\n"
        print(result)

    def recursive_find_max_prefix(self, current_node, prefix):
        i = 0
        indexes_of_nodes = []
        while i < len(current_node.next):
            if current_node.next[i] is not None:
                indexes_of_nodes.append(i)
            i += 1
        if len(indexes_of_nodes) == 1:
            if current_node.value is True:
                return prefix
            prefix += self.get_letter(indexes_of_nodes[0])
            return self.recursive_find_max_prefix(current_node.next[indexes_of_nodes[0]], prefix)
        else:
            return prefix

    def find_max_prefix(self):
        prefix = self.recursive_find_max_prefix(self.root, "")
        if prefix != "":
            return prefix
        return "-"


num = int(input().strip())
prefix_tree = Trie()

for _ in range(num):
    word = input()
    prefix_tree.put(word)
prefix_tree.print_trie()
