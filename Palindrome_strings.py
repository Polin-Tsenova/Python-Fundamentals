words = input().split()
palindrome = input()

def is_palindrome(word):
    return word == word[::-1]

palindrome_words = [word for word in words if is_palindrome(word)]
print(palindrome_words)
palindrome_count =palindrome_words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")