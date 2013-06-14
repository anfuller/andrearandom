from collections import defaultdict
import random

#opening my text file of words
with open('all_words.txt') as f:
    content = f.read()

new_lines = content.split(' ')

# opening my fiels so I can rewrite them
open('two_letters.txt', 'w')
open('seven_letters.txt', 'w')
open('three_letters.txt', 'w')

# getting only the 2, 3, and 7 letter words
for line in new_lines:
    if len(line) == 2:
        with open('two_letters.txt', 'a') as f:
            f.write(line + '\n')
    if len(line) == 3:
        with open('three_letters.txt', 'a') as f:
            f.write(line + '\n')
    if len(line) == 7:
        with open('seven_letters.txt', 'a') as f:
            f.write(line + '\n')

# opening 7 letter file
with open('seven_letters.txt') as f:
    content = f.read()

# making it a list
new_lines = content.split('\n')

# jumbling the letters
anagrams = []
words = []
for line in new_lines:
    anagram = ''.join(sorted(line))
    anagrams.append(anagram)
    words.append(line)

# getting our new lists of all words and their anagrams
anagrams = anagrams[0:len(anagrams)-1]
words = words[0:len(words)-1]

# doing a group by
d = defaultdict(list)
for a, w in zip(anagrams, words):
    d[a].append(w)

matches = [[a, '|'.join(w)] for a, w in d.items()]

# only looking at words that have at least 3 matches. There are 685, FYI
newmatches = []
for item in matches:
    words = str(item[1:2]).count('|')
    if words > 1:
        newmatches.append(item)

#these are our new lists
answers = [x[1] for x in newmatches]
anagrams = [x[0] for x in newmatches]

correct_answers = 0
wrong_answers = 0
for word in anagrams[0:3]:
#getting a random word
    random_word = random.choice(anagrams)
    list_place = anagrams.index(random_word)
    matching_answers = answers[int(list_place)]
    matching_answers = matching_answers.split('|')
    answer = raw_input(random_word + '\n' + str(len(matching_answers)) + ' bingoes\n')
    if answer in matching_answers:
        print "Yes!\n" + ', '.join(matching_answers) + '\n'
        correct_answers = correct_answers + 1
    else:
        print "No!\n" + ','.join(matching_answers) + '\n'
        wrong_answers = wrong_answers + 1

print "You got " + str(correct_answers) + " right and " + str(wrong_answers) + " wrong!"
