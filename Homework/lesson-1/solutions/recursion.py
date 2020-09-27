def maximum(current_max, input_list):

    if len(input_list) == 0:
        return current_max

    if input_list[0] > current_max:
        return maximum(input_list[0], input_list[1:])

    return maximum(current_max, input_list[1:])


input_list = [1, 2, 55, 4, 9]
print(maximum(input_list[0], input_list))