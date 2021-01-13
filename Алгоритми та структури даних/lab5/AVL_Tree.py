class Node:
    def __init__(self, key, value, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0


class AVLTree:
    def __init__(self, key, value):
        self.root = Node(key, value)

    def search(self, key):
        print("searching")
        current = self.root
        while current is not None:
            if key > current.key:
                current = current.right_child
            elif key < current.key:
                current = current.left_child
            elif key == current.key:
                return current.value
        return None

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
            print("got the end")
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

    def insert(self, key, value):
        node = Node(key, value)
        self.root = self.recursively_insert(node, self.root)
        print("inserted")

    def recursive_inorder_traversal(self, tree_node):
        if tree_node is not None:
            self.recursive_inorder_traversal(tree_node.left_child)
            print(f"{tree_node.key} - {tree_node.value}", end=" ")
            self.recursive_inorder_traversal(tree_node.right_child)

    def inorder_traversal(self):
        self.recursive_inorder_traversal(self.root)



