# this opens the file
with open('ellen2.csv', 'U') as f:
    # this is our header row
    header = f.readline().strip().split(',')
    # this reads all the lines in the file
    lines = f.readlines()
    # this gets rid of all those pesky new line characters
    lines_clean = [text.strip() for text in lines]
    # this is our line of integers
    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
                '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
                '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
                '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
                '91', '92', '93', '94', '95', '96', '97', '98', '99']
    # we're looping through this list to find all matches
    for integer in integers:
        #gives each line a line number
        for num, l in enumerate(lines_clean):
            # splits the lines along commas as lists
            ints = l.split(',')
            # gives each position in the list a number
            # remember that python is 0-indexed
            for i, intg in enumerate(ints):
                # finds a integer.
                if intg == integer:
                    # gets the subsequent line with number matches
                    matching_line = lines_clean[num + 1]
                    # splits the matching lines along commas
                    numbers = matching_line.split(',')
                    # gives each number in the matching line a position
                    for i2, l2 in enumerate(numbers):
                        # where the index of the number is the same as integer index
                        # prints the matches
                        if i2 == i:
                            # this also matches it with a header row
                            # now we have the file numer, the person, and their affiliated number
                            results = header[i2] + ',' + integer + ',' + l2 + '\n'
                            # saving results to a file
                            with open('results2.txt', 'a') as f2:
                                f2.write(results)
