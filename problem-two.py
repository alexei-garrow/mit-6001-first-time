# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
bob = 'bob'


def bob_count(s):
    count = 0
    for value in s:
        if value in bob:
            count += 1
    return count

print("Number of times bob occurs is:", bob_count(s))

# GitHub copilot, gave me the direct answer when I asked why bob was udnerlined...

# My own go at a solution from some stack overflow thinking

# def bob_counts(s):
#     words = s.split("   ")
#     print(words)

