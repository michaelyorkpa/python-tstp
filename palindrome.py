def is_palindrome(word):
    word = word.lower()
    return word[::-1]==word

user_word = input("Enter a word to find out if it\'s a palindrome: ")
result=is_palindrome(user_word)
print(result)