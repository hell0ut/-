class Node:
    def __init__(self):
        self.value = None
        self.next = [None] * Tree.R
        self.quantity = 0
        self.first_index = None


class Tree:
    R = 26

    def __init__(self):
        self.root = Node()

    def put(self, key, value):
        self.__put(self.root, key, value, 0)

    def __put(self, node, key, value, d):
        if node is None:
            node = Node()
        if d == len(key):
            node.value = value
            return node
        index = ord(key[d]) - ord("a")
        if node.next[index] is None:
            node.quantity += 1
            node.first_index = index
        node.next[index] = self.__put(node.next[index], key, value, d + 1)
        return node

    def get_max_pref(self, node=None):
        if node is None:
            node = self.root
            if node.quantity != 1:
                return '-'
        if node.quantity == 1:
            index = node.first_index
            return chr(index + ord('a')) + self.get_max_pref(node.next[index])
        if node.quantity != 1:
            return ''

    def get_tree_pic(self, node=None, letter=None):
        if node is None:
            node = self.root
        if letter is None:
            letter = "*"
        if node.quantity == 0:
            return [letter, ]

        elif node.quantity == 1:
            child_lines = self.get_tree_pic(node.next[node.first_index], self.get_letter(node.first_index))
            i = 0
            while i < (len(child_lines)):
                if child_lines[i][0] != ' ':
                    child_lines[i] = letter + '\u2500'*3 + child_lines[i]
                else:
                    child_lines[i] = ' '*4 + child_lines[i]
                i += 1
            return child_lines

        else:
            picture = []
            quantity = 0
            for i in range(len(node.next)-1, -1, -1):
                if node.next[i] is not None:
                    quantity += 1
                    child_tree = self.get_tree_pic(node.next[i], self.get_letter(i))
                    picture.extend(child_tree)
                    picture.append(' ')
            picture = picture[:-1]

            return self.connect_children(picture, quantity, letter)

    @staticmethod
    def connect_children(picture, quantity, letter):
        count = 0
        flag = True
        for i in range(len(picture)):

            if picture[i][0] == ' ':
                if flag:
                    picture[i] = ' ' * 4 + picture[i]
                else:
                    picture[i] = '  \u2502 ' + picture[i]
            else:
                if count == 0:
                    picture[i] = '  \u250c\u2500' + picture[i]
                    flag = False
                elif count == quantity - 1:
                    picture[i] = '  \u2514\u2500' + picture[i]
                    flag = True
                else:
                    picture[i] = '  \u251c\u2500' + picture[i]
                count += 1
        index = len(picture) // 2
        if picture[index][2] == '\u251c':
            picture[index] = letter + '\u2500\u253c' + picture[index][3:]
        else:
            picture[index] = letter + '\u2500\u2524' + picture[index][3:]
        return picture

    @staticmethod
    def get_letter(index):
        return chr(index + ord('a'))

    def __str__(self):
        return '\n'.join(self.get_tree_pic())


if __name__ == '__main__':
    words_count = int(input().strip())

    my_tree = Tree()

    for _ in range(words_count):
        my_tree.put(input(), None)
    print(my_tree)