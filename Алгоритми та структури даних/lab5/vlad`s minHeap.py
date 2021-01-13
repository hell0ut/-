class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.build_min_heap()

    @staticmethod
    def parent(i):
        return i // 2

    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    def size(self):
        return len(self.arr)


    def min_child(self, i):
        left = Heap.left(i)
        right = Heap.right(i)
        length = self.size()
        smallest = i
        if left < length and self.arr[i] > self.arr[left]:
            smallest = left
        if right < length and self.arr[smallest] > self.arr[right]:
            smallest = right
        return smallest

    def sift_down(self, i):
        while True:
            min_child = self.min_child(i)
            if i == min_child:
                break
            self.arr[i], self.arr[min_child] = self.arr[min_child], self.arr[i]
            i = min_child

    def build_min_heap(self):
        for i in reversed(range(len(self.arr) // 2)):
            self.sift_down(i)

    def sift_up(self, i):
        while i > 0:
            parent = Heap.parent(i)
            if self.arr[i] < self.arr[parent]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent

    def insert(self, e):
        self.arr.append(e)
        self.sift_up(self.size() - 1)

    def delete_min(self):
        if self.size() == 0:
            return None
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        head = self.arr.pop()
        if self.size() > 0:
            self.sift_down(0)
        return head


def cookies(k, list_of_sweetness):
    min_heap = Heap(list_of_sweetness)
    num_of_operations = 0
    while min_heap.arr[0] < k:
        if min_heap.size() <= 1:
            return -1
        minimum = min_heap.delete_min()
        second_minimum = min_heap.delete_min()
        new_sweetness = minimum + second_minimum * 2
        min_heap.insert(new_sweetness)
        num_of_operations += 1
    return num_of_operations


n_and_k = input().split()
n = int(n_and_k[0])
k = int(n_and_k[1])
a = [0]
a += list(map(int, input().rstrip().split()))
if len(a) < 1:
    print(-1)
else:
    result = cookies(k, a)
    print(result)

