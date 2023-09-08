#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    if length > 0:
        fibonacci_list.append(0)
        if length > 1:
            fibonacci_list.append(1)
            while len(fibonacci_list) < length:
                num = fibonacci_list[-1] + fibonacci_list[-2]
                fibonacci_list.append(num)
    print(fibonacci_list)
print_fibonacci(9)