class Set:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.container = [None] * self.capacity

    def hasher(self, value):
        return value % self.capacity

    def add(self, value):  # O(1)
        if self.size / self.capacity >= 0.5:
            self.resize(2)
        index = self.hasher(value)
        if self.container[index] is None:
            self.container[index] = value
            self.size += 1
        elif self.container[index] == value:
            pass
        else:
            while True:
                index = self.hasher(index + 1)
                if self.container[index] == value:
                    break
                elif self.container[index] is None:
                    self.container[index] = value
                    self.size += 1
                    break

    def __contains__(self, item):
        index = self.hasher(item)
        if self.container[index] is None:
            return False
        elif self.container[index] == item:
            return True
        else:
            while True:
                index = self.hasher(index + 1)
                if self.container[index] == item:
                    return True
                elif self.container[index] is None:
                    return False

    def resize(self, kof):  # O(n) if line 48 is O(1)
        self.capacity *= kof
        old_size = self.size
        old_container = self.container
        self.container = [None] * self.capacity
        self.size = 0
        for item in old_container:
            if item is not None:
                self.add(item)

    def print(self):
        output = ""
        for item in self.container:
            if item is not None:
                output += str(item) + " "
        print(output)


class InvertedIndex:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hasher(self, key):
        hash_code = 0
        for letter in key:
            hash_code = ord(letter) + hash_code * 31
        return hash_code

    def indexer(self, key):
        return self.hasher(key) % self.capacity

    def put(self, word, value):
        if self.size / self.capacity >= 0.5:
            self.resize(2)
        index = self.indexer(word)
        if self.keys[index] == word:
            self.values[index] = value
        else:
            while self.keys[index] is not None:
                index = (index + 1) % self.capacity
                if self.keys[index] == word:
                    self.values[index] = value
                    return
            self.keys[index] = word
            self.values[index] = value
            self.size += 1

    def index_word(self, word, document_id):
        if self.size / self.capacity >= 0.5:
            self.resize(2)
        index = self.indexer(word)
        if self.keys[index] == word:
            self.values[index].add(document_id)
        else:
            while self.keys[index] is not None:
                index = (index + 1) % self.capacity
                if self.keys[index] == word:
                    self.values[index].add(document_id)
                    return
            self.keys[index] = word
            s = Set()
            s.add(document_id)
            self.values[index] = s
            self.size += 1

    def index_document(self, document, document_id):
        words = document.strip().split()
        for word in words:
            self.index_word(word, document_id)

    def search(self, word):
        index = self.indexer(word)
        if self.keys[index] == word:
            return self.values[index]
        else:
            while self.keys[index] is not None:
                index += 1
                if self.keys[index] == word:
                    return self.values[index]
            return -1

    def get_average_documents_per_key(self):
        number_of_doc = 0
        for s in self.values:
            if s is not None:
                number_of_doc += s.size
        return round(number_of_doc / self.size)

    def resize(self, kof):
        self.capacity *= kof
        self.size = 0
        old_keys = self.keys
        old_values = self.values
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        index = 0
        while index < len(old_keys):
            if old_keys[index] is not None:
                self.put(old_keys[index], old_values[index])
            index += 1


num_documents = int(input().strip())
invind1 = InvertedIndex(10)
for docID in range(num_documents):
    document = input()
    invind1.index_document(document, docID)
num_queries = int(input().strip())
for q in range(num_queries):
    queries_item = input()
    set1 = invind1.search(queries_item)
    if set1 == -1:
        print(-1)
    else:
        set1.print()
print(invind1.get_average_documents_per_key())