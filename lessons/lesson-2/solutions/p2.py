import sys


def apply(func, input_list):
    return_list = [func(item) for item in input_list]
    return return_list


def capitalize(word):
    if type(word) == str:
        return word[0].upper() + word[1:]
    return word


def increment(number):
    if type(number) == int:
        return number + 1
    return number


def special_sum(input_list):
    int_sum = 0
    str_sum = ''
    for item in input_list:
        if type(item) == str:
            str_sum += item
        if type(item) == int:
            int_sum += item
    input_list.append(str_sum + str(int_sum))
    return input_list


if __name__ == '__main__':
    input_list = [1, 2, 'some', 'happy', 33, 'mango']

    print('input list: {}'.format(input_list))
    print('capitalize: {}'.format(apply(capitalize, input_list)))
    print('increment: {}'.format(apply(increment, input_list)))
    print('special sum: {}'.format(special_sum(input_list)))
