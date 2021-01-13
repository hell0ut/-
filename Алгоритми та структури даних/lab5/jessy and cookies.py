
class MinimalHeap:
    root_index = 0

    def __init__(self, container):
        self.container = container
        self.heap_builder()

    def size(self):
        return len(self.container)

    @staticmethod
    def parent(index):
        if index < 1:
            return None
        return (index - 1) // 2

    def child(self, index, direction):  # l - left, something else - right
        if direction == 'l':
            l_child = index * 2 + 1
            if l_child < self.size():
                return l_child
            return None
        else:
            r_child = index * 2 + 2
            if r_child < self.size():
                return r_child
            return None

    def smallest_node(self, index):
        l_child = self.child(index, 'l')
        r_child = self.child(index, 'r')
        smallest = index
        if l_child is not None and self.container[l_child] < self.container[index]:
            smallest = l_child
        if r_child is not None and self.container[r_child] < self.container[smallest]:
            smallest = r_child
        return smallest

    def down_swap(self, index):
        while True:
            smaller_node = self.smallest_node(index)
            if smaller_node == index:
                break
            else:
                self.container[index], self.container[smaller_node] = self.container[smaller_node], self.container[index]
            index = smaller_node

    def heap_builder(self):
        i = self.size() // 2
        while i >= 0:
            self.down_swap(i)
            i -= 1
        print("built")

    def swap_up(self, index):  #
        while index > 0:
            parent_index = self.parent(index)
            if self.container[index] < self.container[parent_index]:
                self.container[index], self.container[parent_index] = self.container[parent_index],self.container[index]
            else:
                break
            index = parent_index

    def add_node(self, value):
        self.container.append(value)
        self.swap_up(self.size() - 1)

    def pop(self):  #
        if self.size() == 0:
            return None
        else:
            self.container[0], self.container[-1] = self.container[-1], self.container[0]
            minimum = self.container.pop()
            self.down_swap(0)
            return minimum


def cookies(k, list_of_sweetness):
    min_heap = MinimalHeap(list_of_sweetness)
    num_of_operations = 0
    while min_heap.container[0] < k:
        if min_heap.size() <= 1:
            return -1
        minimum = min_heap.pop()
        second_minimum = min_heap.pop()
        new_sweetness = minimum + second_minimum * 2
        min_heap.add_node(new_sweetness)
        num_of_operations += 1
    return num_of_operations


n_and_k = input().split()
n = int(n_and_k[0])
k = int(n_and_k[1])
a = list(map(int, input().rstrip().split()))
if len(a) < 1:
    print(-1)
else:
    result = cookies(k, a)
    print(result)

