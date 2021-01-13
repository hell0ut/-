class MinHeap:
    def __init__(self, container):
        self.container = container
        self.min_heapify()

    def right_child_index(self, index):
        index = index * 2 + 1
        if index < len(self.container):
            return index
        return None

    def left_child_index(self, index):
        index *= 2
        if index < len(self.container):
            return index
        return None

    @staticmethod
    def parent_index(index):
        if index > 1:
            return index // 2
        return None

    def smallest_node(self, index):
        smallest_index = index
        right_index = self.right_child_index(index)
        left_index = self.left_child_index(index)
        if left_index is not None and self.container[left_index] < self.container[index]:
            smallest_index = left_index
        if right_index is not None and self.container[right_index] < self.container[smallest_index]:
            smallest_index = right_index
        return smallest_index

    def swap_down(self, index):
        while True:
            min_index = self.smallest_node(index)
            if min_index == index:
                break
            self.container[min_index], self.container[index] = self.container[index], self.container[min_index]

    def swap_up(self, index):
        while True:
            parent = self.parent_index(index)
            if parent is None or self.container[index] >= self.container[parent]:
                break
            else:
                self.container[parent], self.container[index] = self.container[index], self.container[parent]
            index = parent

    def min_heapify(self):
        index = len(self.container) // 2
        while index >= 0:
            self.swap_down(index)
            index -= 1

    def add(self, value):
        self.container.append(value)
        self.swap_up(len(self.container) - 1)

    def pop(self):
        if len(self.container) == 0:
            return None
        else:
            self.container[0], self.container[-1] = self.container[-1], self.container[0]
            min = self.container.pop()
            self.swap_down(0)
            return min


def cookies(k, list_of_sweetness):
    min_heap = MinHeap(list_of_sweetness)
    num_of_operations = 0
    while min_heap.container[0] < k:
        if len(min_heap.container) <= 1:
            return -1
        minimum = min_heap.pop()
        second_minimum = min_heap.pop()
        new_sweetness = minimum + second_minimum * 2
        min_heap.add(new_sweetness)
        num_of_operations += 1
    return num_of_operations


n_and_k = input().split()
n = int(n_and_k[0])
k = int(n_and_k[1])
a = list(map(int, input().rstrip().split()))
sweatness = [None]
if len(a) < 1:
    print(-1)
else:
    result = cookies(k, a)
    print(result)
