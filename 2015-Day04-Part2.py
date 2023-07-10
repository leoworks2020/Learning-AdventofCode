'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day04-Part2
--- Part Two ---
Now find one that starts with six zeroes.
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-05
Challenge Completion Day:   2023-07-05
'''
#Puzzle Part II

import hashlib

dec_counter = int
str_number = str
hash_object = str
secret_key = str

dec_counter = 0
str_number = ""
secret_key = "bgvyzdsv"

while 0 == 0:
    str_number = secret_key + str(dec_counter)
    hash_object = hashlib.md5(str_number.encode('utf-8'))
    print(f'Current counter value = {dec_counter}')
    print(f'Current hash value = {hash_object.hexdigest()}')
    if hash_object.hexdigest()[0:6] == "000000":
        print(f'Found the number! Decimal = {dec_counter}')
        break
    dec_counter += 1