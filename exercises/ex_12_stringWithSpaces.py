"""
Дана строка со словами, которые отделены пробелами.
Убрать из последнего слова все цифры, если есть.
"""

def remove_digits_last_word(s):
    words = s.split()  # split the string into words
    last_word = words[-1]  # get the last word
    last_word = ''.join([c for c in last_word if not c.isdigit()])  # remove any digits
    words[-1] = last_word  # replace the last word with the modified version
    return ' '.join(words)  # join the words back into a string and return it

s = 'Sergey is nice sometimes5.'
print(remove_digits_last_word(s))

##### without 'split' #####

def remove_digits_last_word_adj(s):
    # Find the start and end indices of the last word
    last_word_start = None
    last_word_end = None

    i = len(s) - 1

    while i >= 0:
        if s[i] == ' ':
            if last_word_end is not None:
                last_word_start = i + 1
                break
        else:
            if last_word_end is None:
                last_word_end = i + 1
        i -= 1

    # If the last word contains digits, remove them
    if last_word_end is not None:
        new_last_word = ''
        i = last_word_end - 1
        while i >= last_word_start:
            if not s[i].isdigit():
                new_last_word = s[i] + new_last_word
            i -= 1
        if new_last_word:
            return s[:last_word_start] + new_last_word
        else:
            return s[:last_word_start]
    else:
        return s

s = 'Sergey is nice sometimes5.'
print(remove_digits_last_word_adj(s))  # prints "Sergey is nice sometimes."

"""
In this implementation, we first find the start and end 
indices of the last word in the input string. We initialize 
the last_word_start and last_word_end variables to None, 
and then use a while loop to iterate over the characters 
in the string from the end to the beginning. 

We check each character to see if it is a space or a non-space character, 
and update the last_word_start and last_word_end variables 
accordingly.

If the last word contains digits, we remove them by 
iterating over the characters in the last word from right to 
left. We use another while loop to do this. If a character 
is not a digit, we add it to a new string new_last_word. 
After the loop, we check if new_last_word is non-empty. 

If it is, we concatenate the parts of the string before 
the last word and new_last_word to create the final output. 
If new_last_word is empty, we simply remove the last word 
from the string by returning the part of the string before it. If the input string does not contain any words, the function returns the original string.
"""