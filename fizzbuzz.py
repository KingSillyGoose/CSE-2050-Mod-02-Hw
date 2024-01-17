###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizzbuzz(start, finish):
    """Given two numbers (start, finish) that act as parameters, print every number from start to finish under the following ruleset:
       1. If a number contains a 3 and a 5 or is a multiple of both 3 and 5, print 'fizzbuzz' in place of the number.
       2. If a number contains a 3 or is a multiple of 3, print 'fizz' in place of the number.
       3. If a number contains a 5 or is a multiple of 5, print 'buzz' in place of the number.
       4. Otherwise, if none of these conditions are met, print the number itself.
    
       Args:
        start: The first parameter for the range of numbers.
        finish: The second parameter for the range of numbers.

       Returns:
        Does not return anything, but prints out all numbers or words in range of 'start' and 'finish'.
    """
    for number in range(start, finish + 1):
        if ((number % 3 == 0) and (number % 5 == 0)) or (('3' and '5') in str(number)):  # see rule 1
            print('fizzbuzz')
        elif (number % 3 == 0) or ('3' in str(number)):  # see rule 2
            print('fizz')
        elif (number % 5 == 0) or ('5' in str(number)):  # see rule 3
            print('buzz')
        else:
            print(number)  # see rule 4

#  test cases
fizzbuzz(1, 35)
print(fizzbuzz.__doc__)
