import re
#Write a regex to check if a string contains only digits.
re.fullmatch(r'\d+', "12345")

#Write a pattern to match a 10-digit mobile number.
print(bool(re.fullmatch(r'\d{10}', "9876543210")))

#Find all lowercase letters in a string.
print(bool(re.search(r'[a-z]', "AbCd")))

#Extract all uppercase letters from a sentence.
print(bool(re.search(r'[A-Z]', "Hello ")))
#Match a string that starts with "Hello".
print(bool(re.search(r'^Hello', "Hello Priyadarshee")))
#Match a string that ends with "world".
print(bool(re.search(r'world$', "Hello world")))
#Find all words separated by spaces.
print(bool(re.search(r'\w+\s\w+', "Python is")))
#Match exactly 5 characters.
print(bool(re.fullmatch(r'.{5}', "Hello")))
#Find all occurrences of the word "python" (case-sensitive).
print(bool(re.search(r'python', "I love python")))
#Replace all spaces in a string with underscores.
print(re.sub(r'\s+', '_', "Hello world"))




