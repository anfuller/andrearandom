from collections import defaultdict

# opening 7 letter file
with open('seven_letters.txt') as f:
    content = f.read()

open('anagrams_7s.txt', 'w')

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
    results = a, w
    results2 = ','.join(results)
    with open('anagrams_7s.txt', 'a') as f:
        f.write(results2 + '\n')
