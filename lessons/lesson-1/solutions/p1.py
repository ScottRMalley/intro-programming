import sys

numbers = sys.argv

maximum = 0

if len(numbers) < 2:
    print('Please add some numbers to the command line input')
else:
    for i in range(1, len(numbers)):
        if int(numbers[i]) > maximum:
            maximum = int(numbers[i])
    print('Maximum = ' + str(maximum))
