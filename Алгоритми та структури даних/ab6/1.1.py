def maximum(array):
    max_item = array[0]
    for item in array:
        if item > max_item:
            max_item = item
    return max_item


def find_max_series(array):
    length_array = []
    i = 1
    length_array.append(1)
    while i < len(array):
        j = 0
        length_array.append(1)
        while j < i:
            if array[j] < array[i] and length_array[i] < length_array[j] + 1:
                length_array[i] = length_array[j] + 1
            j += 1
        i += 1
    #print(length_array)
    return maximum(length_array)


if __name__ == "__main__":
    n = input()
    ni = list(map(int, input().rstrip().split()))
    print(find_max_series(ni))

