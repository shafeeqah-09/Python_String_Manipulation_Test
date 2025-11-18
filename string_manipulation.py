from datetime import datetime
# --- Easy ---

def to_uppercase(input_string):
    """Converts a string to uppercase."""
    return input_string.upper()

def to_lowercase(input_string):
    """Converts a string to lowercase."""
    return input_string.lower()

def count_char(input_string, char_to_count):
    """Counts the number of times a character appears in a string."""
    characters=input_string.count(char_to_count)
    return characters 

# --- Medium ---

def reverse_string(input_string):
    """Reverses a string."""
    reversed_string = input_string[::-1]
    return reversed_string


def reverse_sentence(input_string):
    """Reverses the order of words in a sentence."""
    new_string = input_string.split(" ")
    print(new_string)
    new_string.reverse()
    new_list = []
    for i in new_string:
        if i != "":
            new_list.append(i)

    rev =" ".join(new_list)
    return rev

def is_palindrome(input_string):
    """
    Checks if a string is a palindrome.
    Should be case-insensitive and ignore spaces/punctuation.
    """
    palindrome_reverse = input_string.replace(" ","").lower()
    palindrome_reverse = palindrome_reverse.replace(",","")
    palindrome_reverse = palindrome_reverse.replace(":","")
    palindrome_reverse = palindrome_reverse.replace("?","")
    palindrome_reverse = palindrome_reverse.replace(".","")
    palindrome_reverse = palindrome_reverse.replace("'","")
    if palindrome_reverse[::-1] == palindrome_reverse:
        return True 
    else:
        return False 

    pass

# --- Hard ---

def is_anagram(string1, string2):
    """
    Checks if two strings are anagrams.
    Should be case-insensitive and ignore spaces.
    """
    letters = "abcdefghijklmnopqrstuvwxyx0123456789"
    string1 = string1.lower()
    string2 = string2.lower()

    letters2 = ""
    for i in string1:
        if i in letters:
            letters2 += i 

    letters3 = ""
    for i in string2:
        if i in letters:
         letters3 += i

    if sorted(letters2) == sorted(letters3):
        return True 
    else: 
        return False 
    pass

def format_date(date_string):

    formatted = date_string.strftime("%#m/%#D/%#y")
    return formatted
    """
    Converts a date string like "13 november 2025" to "13/11/2025".
    Should handle different capitalizations and month formats.
    """
    pass