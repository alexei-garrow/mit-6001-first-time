#  Problem 1
# 0.0/10.0 points (graded)

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl'
#  your program should print:

# Number of vowels: 5

# no const or let?

#need the syntax for a function? Then how to return it..

s = 'azcbobobegghakl'
vowels = 'aeiou' # avoid the name list as close to list()
# count = 0 Should be inside the function in Python?

# def valid_vowels(s):
#     count = 0 # Need to have count inside the function?
#     for x in s:
#         if x == 'a':
#             count += 1
#         elif x == 'e':
#             count += 1
#         elif x == 'i':
#             count += 1
#         elif x == 'o':
#             count += 1
#         elif x == 'u':
#             count += 1
        
#     return count

# print(valid_vowels(s))

def valid_vowels(s):
    count = 0
    for x in s:
        if x in vowels:
            count += 1
    return count

print("Number of vowels:", valid_vowels(s))

# Crazy version!? Look into it later sum()

# count = sum(1 for char in s if char in vowels)
# print("Number of vowels:", count)








# Co-pilot hype
# If you're ever unsure about syntax or structure, try writing it in plain English first:
# “For each character in the string, if it’s a vowel, add 1 to the count.”

# Then translate that into Python — just like you did. You're thinking like a programmer already. 💡
# Want to try writing a version that counts consonants next?
