def is_palindrome(num):
    if num <= 0:
        raise ValueError("non positive number((")
    orig = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return orig == reversed_num