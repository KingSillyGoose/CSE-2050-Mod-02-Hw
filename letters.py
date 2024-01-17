
def count_letters(file):
    """The following function takes in a file as a parameter and returns the count of all alphabetical letters.
    The function does not count numbers or symbols or anything besides the letters of the alphabet, and is not case sensitive.
    The function only returns counts for letters present within the text file.
    
    Args:
        file: A file that is given through the function call. Contains any amount of text.
    returns:
        The program returns a dictionary of all present letters, with the key being the letter and the value being an integer value of the letters.
    """
    character_dictionary = {}
    with open(file, "r") as upload_file:
        file_text = upload_file.read().lower()  # converts all of the file text into lowercase letters
        for line in file_text:
            for character in line:  # lines 16 + 17 allow the function to check each letter of the text file
                if character.isalpha() == True:  # checks that each character is an a - z letter
                    character_dictionary.update({character: file_text.count(character)})  # creates the dictionary of key value pairs
                else:
                    pass
    return character_dictionary

#  test cases
#  print(count_letters('frost.txt'))
