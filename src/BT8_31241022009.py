# 1.Write a Python function to find the maximum of three numbers.
def maximum(a,b,c):
    return max(a,b,c)
# 2.Write a Python function to sum all the numbers in a list.
def sum(a,b,c):
    return a+b+c
# 3.Write a Python program to reverse a string.
def reverse(str):
    return str[::-1]
# 4.Write a Python function to calculate the factorial of a number (a non-negative integer)
# The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        return "Not exist"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
from math import sqrt
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
        return True
# 6.Write a Python function to print
#   1.all prime numbers that less than a number (enter prompt keyboard).
#   2.the first N prime numbers
def print_prime_under_num(n: int):
    for i in range(2,n):
        if is_prime(i):
            print(i, end=", ")
    print()
def print_n_prime(n: int):
    dem =0
    so =0
    while dem<n:
        if is_prime(so):
            print(so, end=", ")
            dem +=1
        so +=1
    print()
# 7.Write a Python function to check whether a number is "Perfect" or not.
# Then print all perfect number that less than 1000.
def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = 1
    for i in range(2, num//2 + 1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

# 8.Write a Python function to check whether a string is a pangram or not.
#(Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())



if __name__ == '__main__':
    x, y, z = input("#Enter three numbers: ").split()
    x, y, z = int(x), int(y), int(z)
    print(f"1) Maximum of three numbers: {maximum(x,y,z)}")
    print(f"2) Sum of three numbers: {sum(x,y,z)}")
    s = input("#Enter a string: ")
    print(f"3) Reverse of string: {reverse(s)}")
    print(f"4) Factorial of number {z}: {factorial(z)}")
    print(f"5) Whether number {y} is prime or not? {is_prime(y)}")
    N = int(input("#Enter number N: "))
    print(f"6.1) All prime numbers that less than {N}: ")
    print_prime_under_num(10)
    print(f"6.2) The first {N} prime numbers: ")
    print_n_prime(10)
    print(f"7) Whether number {x} is perfect or not? {is_perfect(x)}")
    print("All perfect number that less than 1000:")
    for i in range(1, 1000):
        if is_perfect(i):
            print(i, end=", ")
    print()
    print(f"8) Example: 'The quick brown fox jumps over the lazy dog': {is_pangram("The quick brown fox jumps over the lazy dog")}")
    print(f"            'Hello world': {is_pangram("Hello world")}")