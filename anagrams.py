
def is_anagram(word1, word2):
    """Given two words, it is determined whether or not the second word is an anagram of the first word. The code will return true under the following conditions:
    1. 'word1' and 'word2' have the same number of characters.
    2. The second word contains the exact same number of the exact same letters of the first word.
    
    Args:
        word1: The first word that is compared to by 'word2'.
        word2: The second word that is compared against 'word1'.

    Returns:
        True if it is an anagram, otherwise false.
    """
    if len(word1) != len(word2):  # checking word length allows function to properly count letters without accident
        return False
    else:
        for letter in list(word1):
            if list(word1).count(letter) != list(word2).count(letter):  #  list casting allows the count function to find the amount of letters in each list
                return False               
        return True    

#  test cases    
is_anagram('anagram', 'nagaram')
print(is_anagram('anagram', 'nagaram'))
print(is_anagram.__doc__)
