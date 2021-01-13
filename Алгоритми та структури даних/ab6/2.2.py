def maximum(a, b):
    if a > b:
        return a
    else:
        return b


def mod(a):
    if a > 0:
        return a
    else:
        return -a


def cost(b_array):
    max_current_sum_i = [0]
    max_current_sum_1 = [0]
    i = 1
    while i < len(b_array):
        max_current_sum_i.append(maximum(max_current_sum_i[i - 1] + mod(b_array[i] - b_array[i - 1]),
                                         max_current_sum_1[i - 1] + mod(b_array[i] - 1)))
        max_current_sum_1.append(maximum(max_current_sum_1[i - 1], max_current_sum_i[i - 1] + mod(1 - b_array[i - 1])))
        i += 1
    return maximum(max_current_sum_i[i - 1], max_current_sum_1[i - 1])


if __name__ == "__main__":
    print(len("abc"))

