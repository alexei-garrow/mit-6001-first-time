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
count = 0

def valid_vowels(s):
    for x in s:
        count = 0 # Need to have count inside the function?
        if x == 'a':
            count += 1
        elif x == 'e':
            count += 1
        elif x == 'i':
            count += 1
        elif x == 'o':
            count += 1
        elif x == 'u':
            count += 1
        
    return count

valid_vowels(s)
