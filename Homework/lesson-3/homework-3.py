import numpy

def list_digits(n):
    output_list = []
    while(n > 0):
        last_digit = n % 10
        output_list.append(last_digit)
        n = (n - last_digit)/10

    return output_list[::-1]

def list_to_base_10(b, l):
    current_val = 0
    l = l[::-1]
    for i in range(len(l)):
        current_val += l[i]*(b**i)
    return current_val

def to_base_10(b, n):
    if(b>10):
        return numpy.nan
    digits = list_digits(n)
    return list_to_base_10(b, digits)

if __name__ == "__main__":
    print("Converting number to digits (n = 1011)")
    print(list_digits(1011))
    print("Converting list to base 10 (b = 2, l = [1,0,1,1])")
    print(list_to_base_10(2, [1,0,1,1]))
    print("Converting number to base 10 (b = 2, n = 1011)")
    print(to_base_10(2, 1011))
