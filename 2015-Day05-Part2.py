'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day05-Part2
--- Day 5: Doesn't He Have Intern-Elves For This? ---
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-05
Challenge Completion Day:   2023-07-05
'''
#Puzzle Part II
# TODO: 2023-07-06 - Have done no updates in the code yet...
char_1 = str
char_2 = str
char_3 = str
char_1_and_2 = str
char_1_and_3 = str
items_to_exclude_list = list
excluded_items_list = list
items_nice_list = list
allowed_vowel_list = list
vowel_counter = int
string_position = int
limbo_list = list
string_number = int

#Test only
repeated_letters_list = list
repeated_letters_list = []
double_pair_char_list = list
double_pair_char_list = []


char_1 = ""
char_2 = ""
char_3 = ""
char_1_and_2 = ""
char_1_and_3 = ""
items_to_exclude_list = ['ab', 'cd', 'pq', 'xy']
excluded_items_list = []
items_nice_list = []
allowed_vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0
string_position = 0
limbo_list = []
double_pair_char_list = []
repeated_letters_list = []
string_number = 0

with open("input/2015-Day05-input.txt") as f:
    while True:
        #Read each line of the file
        string = f.readline().strip("\n")

        #Check whether all lines were already processed, if so, leave the while loop
        if not string:
            break
        else:
            string_number += 1
            print(f'Reading String #: {string_number} - {string}')


        ##Check where part of the string is in the items_to_exclude_list
        #for n in range(0,len(items_to_exclude_list)):
        #    if string.find(items_to_exclude_list[n]) >= 0:
        #        print(f'Found an excluded item: {items_to_exclude_list[n]}')
        #        excluded_items_list.append(string)
        #        break

        #Initiating validations for nice items
        if string not in excluded_items_list:
            print(f'Starting Processing...')
            print(f'Checking string: {string}')

            #Scan string chars for comparison
            string_position = 0
            print('Checking for pair of double chars...')
            for c in string:

                #Check whether current char is the last one
                tst = len(string)
                if string_position+2 == len(string)-1:
                    break

                #Capture 3 chars for future comparison
                char_1 = string[string_position]
                char_2 = string[string_position+1]
                char_3 = string[string_position+2]
                char_1_and_2 = char_1 + char_2
                char_1_and_3 = char_1 + char_3

                # Check 1 - Check whether there is a pair of double chars situation
                if string.count(char_1_and_2) >= 2:
                    print(f'Pair of double chars found: {char_1_and_2}. Qty found: {string.count(char_1_and_2)}. Checking for repeated letter now')
                    double_pair_char_list.append(string)
                    print(double_pair_char_list)
                else:
                    print(f'Not able to find pair of double chars...')
                string_position += 1

        # Check 2 - Check for repeated letters with any other letter between them
        if string in double_pair_char_list:
            string_position = 0
            for c in string:
                # Check whether current char is the last one
                if string_position == len(string)-2:
                    break

                #Capture 3 chars for future comparison
                char_1 = string[string_position]
                char_2 = string[string_position+1]
                char_3 = string[string_position+2]
                char_1_and_2 = char_1 + char_2
                char_1_and_3 = char_1 + char_3

                if char_1 == char_3:
                    print(f'Repeated letter found: {char_1}{char_2}{char_3}')
                    repeated_letters_list.append(string)
                    break
                string_position += 1

                #if string in double_pair_char_list:
                #    # Scan string chars for comparison
                #    string_position = 0
                #    #vowel_counter = 0
                #    print(f'Checking for repeated chars...')

                #    for c in string:
                #        # Check wether string is not in double_char_list (Failed Check 1)
                #        if string not in double_pair_char_list:
                #            break

                #        # Check whether current char is the last one
                #        if string_position == len(string):
                #            break

                #        #Check 2 - Check if there is 2 repeated letters with other letter between them
                #        if c in allowed_vowel_list:
                #            print(f'Found vowel: {c}')
                #            vowel_counter += 1

                #            if vowel_counter >= 3:
                #                print('At least three vowels found! Adding to the three_vowels_list...')
                #                three_vowels_list.append(string)
                #                print(three_vowels_list)
                #                break
                #        string_position += 1
        if string not in double_pair_char_list and string not in repeated_letters_list:
            excluded_items_list.append(string)
        if string in double_pair_char_list and string not in repeated_letters_list:
            excluded_items_list.append(string)
        if string not in double_pair_char_list and string in repeated_letters_list:
            excluded_items_list.append(string)
        if string not in excluded_items_list:
            items_nice_list.append(string)
        if string not in excluded_items_list and string not in items_nice_list:
            limbo_list.append(string)

    items_nice_list = list(set(items_nice_list))
    excluded_items_list = list(set(excluded_items_list))
    limbo_list = list(set(limbo_list))
    print(f'END OF PROCESSING...')
    print(f'--------------------')
    print(f'excluded_items_list :')
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


