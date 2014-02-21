#this game quizzes us on two letter combox to see if they're words
import itertools
import random


def scrabble_twos():

    print "\nAre these two-letter combinations valid Scrabble words?\n\
    - Type 'quit' to quit\n\
    - Type 'y' for yes\n\
    - Type 'n' for no\n---"

    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

    words = ['AA', 'AB', 'AD', 'AE', 'AG', 'AH', 'AI', 'AL', 'AM',
             'AN', 'AR', 'AS', 'AT', 'AW', 'AX', 'AY', 'BA', 'BE',
             'BI', 'BO', 'BY', 'DE', 'DO', 'ED', 'EF', 'EH', 'EL',
             'EM', 'EN', 'ER', 'ES', 'ET', 'EX', 'FA', 'FE', 'GO',
             'HA', 'HE', 'HI', 'HM', 'HO', 'ID', 'IF', 'IN', 'IS',
             'IT', 'JO', 'KA', 'KI', 'LA', 'LI', 'LO', 'MA', 'ME',
             'MI', 'MM', 'MO', 'MU', 'MY', 'NA', 'NE', 'NO', 'NU',
             'OD', 'OE', 'OF', 'OH', 'OI', 'OM', 'ON', 'OP', 'OR',
             'OS', 'OW', 'OX', 'OY', 'PA', 'PE', 'PI', 'QI', 'RE',
             'SH', 'SI', 'SO', 'TA', 'TI', 'TO', 'UH', 'UM', 'UN',
             'UP', 'US', 'UT', 'WE', 'WO', 'XI', 'XU', 'YA', 'YE',
             'YO', 'ZA']

#combines consonants and vowels
    combos = list(itertools.product(consonants, vowels)) + list(itertools.product(vowels, consonants))
    correct_answers = 0
    incorrect_answers = 0
    are_words = ''
    not_words = ''
    words_found = ''

#loops through our combox
    for c in combos[0:25]:
        random_item = random.choice(combos)
        text = ''.join(random_item)
        answer = raw_input(text + '\n').lower()

#answers right or wrong
        if answer[0] == 'y' and any(text in w for w in words):
            print "Correct, " + text + " is a word! \n---"
            correct_answers = correct_answers + 1
            words_found = words_found + text + '\n'
        elif answer[0] == 'n' and any(text in w for w in words):
            print "Nope, " + text + " is a word! \n---"
            incorrect_answers = incorrect_answers + 1
            are_words = are_words + text + '\n'
        elif answer[0] == 'n' and any(text not in w for w in words):
            print "Correct, " + text + " is not a word! \n---"
            correct_answers = correct_answers + 1
        elif answer[0] == 'y' and any(text not in w for w in words):
            print "Nope, " + text + " is not a word! \n---"
            incorrect_answers = incorrect_answers + 1
            not_words = not_words + text + '\n'
        elif answer == "quit":
            print "---\nCorrect: ", correct_answers
            print "Incorrect: ", incorrect_answers
# Prevent exception if user types quit without answering any question                    
            try:
                pct_correct = str(int(round(100*float(correct_answers)/float(correct_answers+incorrect_answers), 0)))+"%"
            except:
                pct_correct = "n/a" 
            print "Percent correct: ", pct_correct
            if words_found != '':
                print "\nYou correctly found:\n", words_found
            else:
                pass
            if are_words != '':
                print "Are words:\n", are_words
            else:
                pass
            if not_words != '':
                print "Not words:\n", not_words
            else:
                pass
            quit()
        else:
            print "Invalid answer!\n---"

#printing results
    print "\nCorrect answers: ", correct_answers
    print "Incorrect answers: ", incorrect_answers
    pct_correct = str(int(round(100*float(correct_answers)/float(correct_answers+incorrect_answers), 0)))+"%"
    print "Percent correct: ", pct_correct
    if words_found != '':
        print "\nYou correctly found:\n", words_found
    else:
        pass
    if are_words != '':
        print "These are words:\n", are_words
    else:
        pass
    if not_words != '':
        print "These are not words:\n", not_words
    else:
        pass

scrabble_twos()
