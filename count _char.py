def count_characters(string):
    count_dict = {}
    string = string.lower()
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    return count_dict

user_string=input("Enter a sentence: ")
result=count_characters(user_string)
print(result)