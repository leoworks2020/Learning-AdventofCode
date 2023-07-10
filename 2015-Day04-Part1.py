'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day04-Part1
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is bgvyzdsv.
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-05
Challenge Completion Day:   2023-07-05
'''
#Puzzle Part I

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
    if hash_object.hexdigest()[0:5] == "00000":
        print(f'Found the number! Decimal = {dec_counter}')
        break
    dec_counter += 1