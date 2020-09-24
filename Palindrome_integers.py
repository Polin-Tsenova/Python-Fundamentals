def is_palindrome(num):
    reversed_num = num[::-1]
    is_palindrome = True
    if num != reversed_num:
        is_palindrome = False

    return is_palindrome


numbers_list = input().split(", ")

for n in numbers_list:
    print(is_palindrome(n))

