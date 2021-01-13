class Node:
    def __init__(self, key, value=None, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0


class AVLSet:
    def __init__(self, key):
        self.root = Node(key)
        self.num_of_nodes = 1

    def __contains__(self, key):
        current = self.root
        while current is not None:
            if key > current.key:
                current = current.right_child
            elif key < current.key:
                current = current.left_child
            elif key == current.key:
                return True
        return False

    @staticmethod
    def current_height(tree_node):  # -1 if tree_node does not exist
        if tree_node is not None:
            return tree_node.height
        else:
            return -1

    def left_rotation(self, pivot):
        local_root = pivot.right_child
        pivot_child = local_root.left_child
        local_root.left_child = pivot
        pivot.right_child = pivot_child
        pivot.height = max(self.current_height(pivot.left_child), self.current_height(pivot.right_child)) + 1
        local_root.height = max(self.current_height(local_root.left_child), self.current_height(local_root.right_child)) + 1
        return local_root

    def right_rotation(self, pivot):
        local_root = pivot.left_child
        pivot_child = local_root.right_child
        local_root.right_child = pivot
        pivot.left_child = pivot_child
        pivot.height = max(self.current_height(pivot.left_child), self.current_height(pivot.right_child)) + 1
        local_root.height = max(self.current_height(local_root.left_child), self.current_height(local_root.right_child)) + 1
        return local_root

    def recursively_insert(self, node, tree_node):  # inserting a node
        if tree_node is None:
            self.num_of_nodes += 1
            return node
        elif tree_node.key > node.key:
            tree_node.left_child = self.recursively_insert(node, tree_node.left_child)
        elif tree_node.key < node.key:
            tree_node.right_child = self.recursively_insert(node, tree_node.right_child)
        else:
            tree_node.value = node.value
        tree_node.height = max(self.current_height(tree_node.left_child), self.current_height(tree_node.right_child)) + 1
        balance = 0
        if tree_node is not None:
            balance = self.current_height(tree_node.left_child) - self.current_height(tree_node.right_child)
        if balance > 1:
            if node.key < tree_node.left_child.key:
                tree_node = self.right_rotation(tree_node)
            else:
                tree_node.left_child = self.left_rotation(tree_node.left_child)
                return self.right_rotation(tree_node)
        if balance < -1:
            if node.key > tree_node.right_child.key:
                tree_node = self.left_rotation(tree_node)
            else:
                tree_node.right_child = self.right_rotation(tree_node.right_child)
                return self.left_rotation(tree_node)
        return tree_node

    def insert(self, key, value=None):
        node = Node(key, value)
        self.root = self.recursively_insert(node, self.root)

    def recursive_inorder_traversal(self, tree_node):
        if tree_node is not None:
            self.recursive_inorder_traversal(tree_node.left_child)
            print(tree_node.key, end=" ")
            self.recursive_inorder_traversal(tree_node.right_child)

    def inorder_traversal(self):
        self.recursive_inorder_traversal(self.root)


class AVLInvertedIndex:
    def __init__(self,root=None):
        self.root = root
        self.num_of_nodes = 0

    def search(self, key):
        current = self.root
        while current is not None:
            if key > current.key:
                current = current.right_child
            elif key < current.key:
                current = current.left_child
            elif key == current.key:
                return current.value
        return -1

    @staticmethod
    def current_height(tree_node):  # -1 if tree_node does not exist
        if tree_node is not None:
            return tree_node.height
        else:
            return -1

    def left_rotation(self, pivot):
        local_root = pivot.right_child
        pivot_child = local_root.left_child
        local_root.left_child = pivot
        pivot.right_child = pivot_child
        pivot.height = max(self.current_height(pivot.left_child), self.current_height(pivot.right_child)) + 1
        local_root.height = max(self.current_height(local_root.left_child), self.current_height(local_root.right_child)) + 1
        return local_root

    def right_rotation(self, pivot):
        local_root = pivot.left_child
        pivot_child = local_root.right_child
        local_root.right_child = pivot
        pivot.left_child = pivot_child
        pivot.height = max(self.current_height(pivot.left_child), self.current_height(pivot.right_child)) + 1
        local_root.height = max(self.current_height(local_root.left_child), self.current_height(local_root.right_child)) + 1
        return local_root

    def recursively_index_word(self, node, tree_node):  # inserting a node
        if tree_node is None:
            self.num_of_nodes += 1
            node.value = AVLSet(node.value)  # making a set from doc_id and adding it if the word has not been indexed
            return node
        elif tree_node.key > node.key:
            tree_node.left_child = self.recursively_index_word(node, tree_node.left_child)
        elif tree_node.key < node.key:
            tree_node.right_child = self.recursively_index_word(node, tree_node.right_child)
        else:
            tree_node.value.insert(node.value)  # adding an doc_id if the word already indexed
            # balancing
        tree_node.height = max(self.current_height(tree_node.left_child), self.current_height(tree_node.right_child)) + 1
        balance = 0
        if tree_node is not None:
            balance = self.current_height(tree_node.left_child) - self.current_height(tree_node.right_child)
        if balance > 1:
            if node.key < tree_node.left_child.key:
                tree_node = self.right_rotation(tree_node)
            else:
                tree_node.left_child = self.left_rotation(tree_node.left_child)
                return self.right_rotation(tree_node)
        if balance < -1:
            if node.key > tree_node.right_child.key:
                tree_node = self.left_rotation(tree_node)
            else:
                tree_node.right_child = self.right_rotation(tree_node.right_child)
                return self.left_rotation(tree_node)
        return tree_node

    def index_word(self, key, value):
        node = Node(key, value)
        self.root = self.recursively_index_word(node, self.root)

    def index_document(self, document, document_id):
        words = document.strip().split()
        for word in words:
            self.index_word(word, document_id)

    def get_num_of_docs(self, tree_node):
        num_of_docs = 0
        if tree_node is not None:
            num_of_docs += self.get_num_of_docs(tree_node.left_child)
            num_of_docs += tree_node.value.num_of_nodes
            num_of_docs += self.get_num_of_docs(tree_node.right_child)
        return num_of_docs

    def get_average_documents_per_key(self):
        return round(self.get_num_of_docs(self.root) / self.num_of_nodes)

    def recursive_inorder_traversal(self, tree_node):
        if tree_node is not None:
            self.recursive_inorder_traversal(tree_node.left_child)
            print(tree_node.key, end=" ")
            self.recursive_inorder_traversal(tree_node.right_child)

    def inorder_traversal(self):
        self.recursive_inorder_traversal(self.root)


num_documents = int(input().strip())
avl_index_tree = AVLInvertedIndex()
for _ in range(num_documents):
    documents_item = input()
    avl_index_tree.index_document(documents_item, _)
num_queries = int(input().strip())
for _ in range(num_queries):
    queries_item = input()
    output = avl_index_tree.search(queries_item)
    if output == -1:
        print(output)
    else:
        output.inorder_traversal()
        print("\n", end="")
print(avl_index_tree.get_average_documents_per_key())
try:
    print_keys_flag = input()
    should_print_keys = print_keys_flag == 'print_keys'
except:
    should_print_keys = False
if should_print_keys:
    avl_index_tree.inorder_traversal()