def construct_suffix_set(string):
    suffix_set = set()

    for start in range(len(string)):
        suffix_set.add(string[start:])

    return suffix_set


def construct_lcp_array(suffix_array):
    lcp = []
    for i in range(len(suffix_array)):

        if i == 0:
            lcp.append(0)

        if i + 1 == len(suffix_array):
            break

        else:
            common_length = 0

            for char1, char2 in zip(suffix_array[i], suffix_array[i + 1]):
                if char1 == char2:
                    common_length += 1
                else:
                    break
            lcp.append(common_length)

    return lcp


def find_kth_substring(suffix_array, lcp_array, k):
    unique_substr_num = 0
    previous_substr_num = 0

    for suffix, lcp_value in zip(suffix_array, lcp_array):
        unique_substr_num += len(suffix) - lcp_value

        if unique_substr_num - 1 == k:
            return suffix

        elif unique_substr_num - 1 > k:

            for i, j in enumerate(range(lcp_value, len(suffix))):
                if previous_substr_num + i == k:
                    return suffix[:j + 1]

        previous_substr_num = unique_substr_num

    return 'INVALID'


def findStrings(w, queries):

    suffix_arr = set()
    for suffix_set in map(construct_suffix_set, w):
        suffix_arr.update(suffix_set)

    suffix_arr = sorted(list(suffix_arr))
    lcp_arr = construct_lcp_array(suffix_arr)

    return [find_kth_substring(suffix_arr, lcp_arr, q - 1) for q in queries]


if __name__ == '__main__':
    w_count = int(input())

    w = []

    for _ in range(w_count):
        w_item = input()
        w.append(w_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = findStrings(w, queries)

    for substring in result:
        print(substring)
