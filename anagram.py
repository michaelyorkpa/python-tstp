def is_anagram(w1,w2):
    w1=w1.lower()
    w2=w2.lower()
    return sorted(w1) == sorted(w2)

user_word1 = ""
user_word2 = ""

while user_word1 is not "q" and user_word2 is not "q":
    user_word1 = input("Enter word one to find out if it\'s an anagram (q to quit): ")
    user_word2 = input("Enter word two to find out if it\'s an anagram (q to quit): ")
    result = is_anagram(user_word1, user_word2)
    print(result)