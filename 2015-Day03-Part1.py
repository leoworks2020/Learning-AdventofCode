'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day03
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

- > delivers presents to 2 houses: one at the starting location, and one to the east.
- ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
- ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-04
Challenge Completion Day:   2023-07-07
'''
#Puzzle Part I
counter_delivered_houses = int
vertical_position = int
horizontal_position = int
vertical_string = str
horizontal_string = str
current_position = str
house_list = list

#Position is a mask composed of 4 elements: North, East, West, South. It will received converted integer from each position as a concatenated string
current_position = "+0+0"
house_list = [current_position]
vertical_position = 0
horizontal_position = 0
vertical_string = ""
horizontal_string = ""
counter_delivered_houses = 0

print(f'Santa starting at house # {current_position}')

with open("input/2015-Day03-input.txt") as f:
    while True:
        f_line = f.readlines()
        if not f_line:
            break
        #print(f_line)
        f_line = f_line[0]
        for element in f_line:
            # Here position as integer will be added for North and West and reduced for South and West
            if element == "^":
                vertical_position += 1
            elif element == "v":
                vertical_position -= 1
            elif element == ">":
                horizontal_position += 1
            elif element == "<":
                horizontal_position -= 1
            # Here integer position will be converted to string and receive a positive (+) or negative (-) clause for house identification
            if vertical_position >= 0:
                vertical_string = "+" + str(abs(vertical_position))
            else:
                vertical_string = "-" + str(abs(vertical_position))

            if horizontal_position >= 0:
                horizontal_string = "+" + str(abs(horizontal_position))
            else:
                horizontal_string = "-" + str(abs(horizontal_position))

            current_position = str(vertical_string) + str(horizontal_string)
            print(f'Santa is at house number # {current_position}')

            if current_position not in house_list:
                house_list.append(current_position)
            print(f'current position = {current_position}')
    counter_delivered_houses = len(house_list)
    print(f'The total # of houses which received at least one presents = {counter_delivered_houses} ')