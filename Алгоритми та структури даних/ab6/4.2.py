class Node:
    def __init__(self, capacity, value=None):
        self.next = [None] * capacity
        self.value = value
        self.size = 0


class Tree:
    letter_capacity = 26

    def __init__(self):
        self.root = Node(Tree.letter_capacity)
        self.width = 0
        self.hight = 0

    def update_hight(self, new_hight):
        if new_hight > self.hight:
            self.hight = new_hight

    def update_width(self, new_width):
        if new_width > self.width:
            self.width = new_width

    @staticmethod
    def get_index(letter):
        return ord(letter) - ord("a")

    @staticmethod
    def get_letter(index):
        return chr(index + ord("a"))

    def recursive_put(self, word, step, current_node):
        if current_node is None:
            current_node = Node(Tree.letter_capacity)
        if step == len(word):
            current_node.value = True
            self.update_hight(step)
        if step != len(word):
            i = self.get_index(word[step])
            if current_node.next[i] is None:
                current_node.size += 1
                self.update_width(current_node.size)
            current_node.next[i] = self.recursive_put(word, step + 1, current_node.next[i])
        return current_node

    def put(self, word):
        self.root = self.recursive_put(word, 0, self.root)

    def recursive_find(self, word, step, current_node):
        if current_node is None:
            return None
        if step == len(word) - 1:
            return current_node.value
        i = self.get_index(word[step])
        return self.recursive_find(word, step + 1, current_node.next[i])

    def find(self, word):
        return self.recursive_find(word, 0, self.root)

    @staticmethod
    def get_current_letters(current_node_list):
        i = 0
        indexes_of_nodes = []
        while i < len(current_node_list.next):
            if current_node_list.next[i] is not None:
                indexes_of_nodes.append(i)
            i += 1
        return indexes_of_nodes

    @staticmethod
    def crete_matrix(width, height):
        arr = []
        for i in range(height):
            arr.append([' '] * width)
        return arr

    def recursive_paint_tree(self, current_node):
        if current_node is not None:
            letters = self.get_current_letters(current_node.next)
            if len(letters) == 0:
                return [False, []]
            if len(letters) == 1:
                graph_list = self.recursive_paint_tree(current_node.next[letters[0]])
                if not graph_list[0]:
                    graph_list[1].append(self.get_letter(letters[0]))
                    return graph_list
            if len(letters) > 1:
                i = len(letters) - 1
                matrix = []
                while i < 0:
                    array = self.recursive_paint_tree(current_node.next[letters[i]])
                    matrix.append(["─"])
                    j = len(array) - 1
                    while j != -1:
                        matrix[0].append(array[j])
                        if j != 0:
                            for i in range(2):
                                matrix[0].append("─")

    def traversal(self):
        self.__traversal(self.root, 0)

    def __traversal(self, node, x):
        array_of_index = self.get_current_letters(node)
        i = len(array_of_index) - 1
        x += 4
        while i >= 0:
            self.__traversal(node.next[array_of_index[i]], x)
            print(self.get_letter(array_of_index[i]), end=" ")
            i -= 1
        print(x)


tree = Tree()
tree.put("cat")
tree.put("dog")
tree.put("soup")
tree.traversal()
