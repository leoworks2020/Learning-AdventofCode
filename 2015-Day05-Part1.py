'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day05-Part1
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-05
Challenge Completion Day:   2023-07-06
'''
#Puzzle Part I

char_1 = str
char_2 = str
char_1_and_2 = str
items_to_exclude_list = list
excluded_items_list = list
items_nice_list = list
allowed_vowel_list = list
vowel_counter = int
string_position = int
limbo_list = list
string_number = int

#Test only
three_vowels_list = list
three_vowels_list = []
double_char_list = list
double_char_list = []


char_1 = ""
char_2 = ""
char_1_and_2 = ""
items_to_exclude_list = ['ab', 'cd', 'pq', 'xy']
excluded_items_list = []
items_nice_list = []
allowed_vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0
string_position = 0
limbo_list = []
double_char_list = []
three_vowels_list = []
string_number = 0

with open("input/2015-Day05-input.txt") as f:
    while True:
        #Read each line of the file
        string = f.readline().strip("\n")

        #Check wether all lines were already processed, if so, leave the while loop
        if not string:
            break
        else:
            string_number += 1
            print(f'Reading String #: {string_number} - {string}')


        #Check where part of the string is in the items_to_exclude_list
        for n in range(0,len(items_to_exclude_list)):
            if string.find(items_to_exclude_list[n]) >= 0:
                print(f'Found an excluded item: {items_to_exclude_list[n]}')
                excluded_items_list.append(string)
                break

        #Initiating processing
        if string not in excluded_items_list:
            print(f'Starting Processing...')
            print(f'Checking string: {string}')

            #Scan string chars for comparison
            string_position = 0
            print('Checking for double chars...')
            for c in string:

                #Check wether current char is the last one
                if string_position == len(string)-1:
                    break

                #Capture 2 chars for future comparison
                char_1 = string[string_position]
                char_2 = string[string_position+1]
                char_1_and_2 = char_1 + char_2

                # Check 1 - Check wether there is a double char situation
                if char_1 == char_2:
                    print(f'Double char found: {char_1_and_2}. Checking for 3 vowels now')
                    double_char_list.append(string)
                    print(double_char_list)
                string_position += 1

            if string in double_char_list:
                # Scan string chars for comparison
                string_position = 0
                vowel_counter = 0
                print(f'Checking for three vowels...')

                for c in string:
                    # Check wether string is not in double_char_list (Failed Check 1)
                    if string not in double_char_list:
                        break

                    # Check wether current char is the last one
                    if string_position == len(string):
                        break

                    #Check 2 - Check if at least 3 nice vowels exist in the string
                    if c in allowed_vowel_list:
                        print(f'Found vowel: {c}')
                        vowel_counter += 1

                        if vowel_counter >= 3:
                            print('At least three vowels found! Adding to the three_vowels_list...')
                            three_vowels_list.append(string)
                            print(three_vowels_list)
                            break
                    string_position += 1
        if string not in double_char_list and string not in three_vowels_list:
            excluded_items_list.append(string)
        if string in double_char_list and string not in three_vowels_list:
            excluded_items_list.append(string)
        if string not in double_char_list and string in three_vowels_list:
            excluded_items_list.append(string)
        if string in double_char_list and string in three_vowels_list and string not in excluded_items_list:
            print(f'double_char_list: {double_char_list}')
            print(f'three vowels list: {three_vowels_list}')
            items_nice_list.append(string)
            print(f'items_nice_list size = {len(items_nice_list)}')
        if string not in excluded_items_list and string not in items_nice_list:
            limbo_list.append(string)

    items_nice_list = list(set(items_nice_list))
    print(f'items_nice_list size = {len(items_nice_list)}')

    if excluded_items_list == list(set(excluded_items_list)):
        print('There are no duplicates in excluded_items_list')
    else:
        excluded_items_list = list(set(excluded_items_list))
    print(f'END OF PROCESSING...')
    print(f'--------------------')
    print(f'excluded contents :')
    print(excluded_items_list)
    print(f'--------------------')
    print(f'nice-list contents :')
    print(items_nice_list)
    print(f'--------------------')
    print(f'limbo contents :')
    print(limbo_list)
    print(f'--------------------')
    print(f'The total number of nice items = {len(items_nice_list)}')
    print(f'The total number of excluded items = {len(excluded_items_list)}')
    limbo_list = list(set(limbo_list))
    print(f'The total number of limbo = {len(limbo_list)}')
    print(limbo_list)


