import sys
import cProfile
import numpy as np
import time

N = 5000000
test_array = np.random.rand(N)

def mult_for(input_list):
    result = 1
    for num in input_list:
        result = result*num
    return result

def mult_while(input_list):
    result = 1
    i = 0
    while i < len(input_list):
        result = result*input_list[i]
        i += 1
    return result

def mult_recursive(input_list, length):
    if length < 2:
        return input_list[0]
    if length < 3:
        return input_list[0]*input_list[1]
    split = length//2
    return mult_recursive(input_list[:split], split)*mult_recursive(input_list[split:], length - split)

def for_profile():
    return mult_for(test_array)

def while_profile():
    return mult_while(test_array)

def rec_profile():
    return mult_recursive(test_array, N)

def profile(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

if __name__ == '__main__':
    print('---for loop---')
    print(profile(for_profile))
    print('---while loop---')
    print(profile(while_profile))
    print('---recursive---')
    print(profile(rec_profile))
