# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


user_input1 = input("Enter the First word: ")
user_input2 = input("Enter the Second word: ")

print(find_anagram(user_input1, user_input2))