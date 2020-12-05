import sys


def mult_for(input_list):
    result = 1
    for num in input_list:
        result = result * num
    return result


def mult_while(input_list):
    result = 1
    i = 0
    while i < len(input_list):
        result = result * input_list[i]
        i += 1
    return result


def mult_recursive(input_list, length):
    if length < 2:
        return input_list[0]
    if length < 3:
        return input_list[0] * input_list[1]
    split = length // 2
    return mult_recursive(input_list[:split], split) * mult_recursive(input_list[split:], length - split)


if __name__ == '__main__':
    input_list = [int(arg) for arg in sys.argv[1:]]

    print('---for loop---')
    print('Result: {}'.format(mult_for(input_list)))
    print('---while loop---')
    print('Result: {}'.format(mult_while(input_list)))
    print('---recursive---')
    print('Result: {}'.format(mult_recursive(input_list, len(input_list))))
