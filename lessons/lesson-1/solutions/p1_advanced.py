import sys


def maximum(input_list):
    # assume first is the maximum
    m = input_list[0]
    # replace if another is larger
    for j in input_list:
        if j > m:
            m = j
    return m


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print('please provide a list of numbers')
        sys.exit()

    numbers = [int(x) for x in sys.argv[1:]]

    print('maximum: {}'.format(maximum(numbers)))
