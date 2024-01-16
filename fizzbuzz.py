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
    for number in range(start, finish + 1):
        if ((number % 3 == 0) and (number % 5 == 0)) or (('3' and '5') in str(number)):
            print('fizzbuzz')
        elif (number % 3 == 0) or ('3' in str(number)):
            print('fizz')
        elif (number % 5 == 0) or ('5' in str(number)):
            print('buzz')
        else:
            print(number)

fizzbuzz(1, 35)
