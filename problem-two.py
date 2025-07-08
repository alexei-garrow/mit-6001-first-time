# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s: str = 'azcbobobegghakl'
bob: str = 'bob'

# Grabs a count of 5 because it checks each character of bob being 'b' and 'o' 
# def bob_count(s):
#     count = 0
#     for value in s:
#         if value in bob:
#             count += 1
#     return count

# print("Number of times bob occurs is:", bob_count(s))

# GitHub copilot, gave me the direct answer when I asked why bob was underlined...:
# I got it to add the comments as I wanted to understand the answer

# def bob_count(s: str):
#     count: int = 0
#     for i in range(len(s) - 2):  # stop 2 characters before the end
#         if s[i:i+3] == 'bob':    # check 3-character slices
#             count += 1
#     return count

# print("Number of times bob occurs is:", bob_count(s))

# an expansion that shows progress 

def bob_count(s: str) -> int:
    count = 0
    for i in range(len(s) - 2):
        slice = s[i:i+3]
        print(f"Checking slice: {slice}")
        if slice == 'bob':
            count += 1
    return count

s = 'azcbobobegghakl'
print("Number of times bob occurs is:", bob_count(s))



# My own brainstorming at a solution from some stack overflow thinking

# def bob_counts(s):
#     words = s.split("   ") # would only get spaces, and there aren't that many
#     print(words)

