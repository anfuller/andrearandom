from collections import defaultdict
import random

#opening my text file of words
with open('all_words.txt') as f:
    content = f.read()

new_lines = content.split(' ')

words = []
anagrams = []

# getting only the 2, 3, and 7 letter words
for line in new_lines:
    if len(line) == 7\
       and ('T' in line and 'I' in line and 'S' in line and 'A' in line and 'N' in line and 'E' in line):
        anagrams.append(''.join(sorted(line)))
        words.append(''.join(line))

# doing a group by
d = defaultdict(list)
for a, w in zip(anagrams, words):
    d[a].append(w)

matches = 0
total_possible = 0

for a in d.keys()[0:3]:
    anagram = random.choice(d.keys())
    results = d.get(anagram)
    len_results = len(d.get(anagram))
    answer = raw_input(anagram + ' - ' + str(len_results) + ' bingoes:')
    answers = answer.split(', ')
    print '\n' + ', '.join(results) + '\n'
    total_possible = total_possible + len_results
    for a in answers:
        if a in results:
            matches = matches + 1
print str(round(float(matches)/float(total_possible)*100, 0)) + '%'
