import sys

fibonacci_dict = {}


def fibonacci_for(n):
    if n < 2:
        return [1]
    result = [1, 1]
    for k in range(1, n - 1):
        result.append(result[k - 1] + result[k])
    return result


def fibonacci(n):
    if n < 3:
        return 1

    if n in fibonacci_dict:
        return fibonacci_dict[n]

    result = fibonacci(n - 2) + fibonacci(n - 1)
    fibonacci_dict[n] = result
    return result


def fibonacci_rec(n):
    return [fibonacci(i + 1) for i in range(n)]


if __name__ == '__main__':
    n = int(sys.argv[1])
    print('Calculating {} Fibonacci numbers'.format(n))
    print('With for loop')
    print(fibonacci_for(n))
    print('With recursion')
    print(fibonacci_rec(n))
