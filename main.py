# Scenario
# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

# Your task is to write a program which:

# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:

# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

######################################################################################################################
# Test your code using the data we've provided.

# Test data
# Sample input:

# Listen
# Silent

# Sample output:

# Anagrams


# Sample input:

# modern
# norman

# Sample output:

# Not anagrams
######################################################################################################################


def isanag(txt1, txt2):
    if len(txt1) != len(txt2):
        return 0
    txt1 = txt1.lower()
    txt2 = txt2.lower()
    dict1 = {}
    dict2 = {}
    for i in range(len(txt1)):
        dict1[txt1[i]] = dict1.get(txt1[i], 0) + 1
        dict2[txt2[i]] = dict2.get(txt2[i], 0) + 1
    for i in dict1:
        if dict1[i] != dict2[i]:
            return 0
    return 1


txt1 = input("Please enter the first word:\n ")
txt2 = input("Please enter the second word:\n")
# txt1 = "silent"
# txt2 = "listen"
if isanag(txt1, txt2):
    print("Anagrams")
else:
    print("Not anagrams")
