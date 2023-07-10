'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day03
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
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
santa_current_position = str
robot_current_position = str
santa_house_list = list
robot_house_list = list
house_list = list
current_deliver = str

#Position is a mask composed of 4 characters, where 1st two represent a vertical axis (can be positive or negative and 2nd two characteres represent a horizontal axis
santa_current_position = "+0+0"
robot_current_position = "+0+0"
santa_house_list = [santa_current_position]
robot_house_list = [robot_current_position]
house_list = [santa_current_position]
santa_vertical_position = 0
santa_horizontal_position = 0
santa_vertical_string = ""
santa_horizontal_string = ""
robot_vertical_position = 0
robot_horizontal_position = 0
robot_vertical_string = ""
robot_horizontal_string = ""
counter_delivered_houses = 0
current_deliver = "Santa"

print(f'Santa starting at house # {santa_current_position}')
print(f'Robot starting at house # {robot_current_position}')

with open("input/2015-Day03-input.txt") as f:
    while True:
        f_line = f.readlines()
        if not f_line:
            break
        f_line = f_line[0]
        for element in f_line:
            if current_deliver == "Santa":
                # Here position as integer will be added for North and West and reduced for South and West
                if element == "^":
                    santa_vertical_position += 1
                elif element == "v":
                    santa_vertical_position -= 1
                elif element == ">":
                    santa_horizontal_position += 1
                elif element == "<":
                    santa_horizontal_position -= 1
                # Here integer position will be converted to string and receive a positive (+) or negative (-) clause for house identification
                if santa_vertical_position >= 0:
                    santa_vertical_string = "+" + str(abs(santa_vertical_position))
                else:
                    santa_vertical_string = "-" + str(abs(santa_vertical_position))

                if santa_horizontal_position >= 0:
                    santa_horizontal_string = "+" + str(abs(santa_horizontal_position))
                else:
                    santa_horizontal_string = "-" + str(abs(santa_horizontal_position))

                santa_current_position = str(santa_vertical_string) + str(santa_horizontal_string)
                print(f'Santa is at house number # {santa_current_position}')
                if santa_current_position not in santa_house_list:
                    santa_house_list.append(santa_current_position)
                #replacing deliver person for next iteration
                current_deliver = "Robot"
            elif current_deliver == "Robot":
                # Here position as integer will be added for North and West and reduced for South and West
                if element == "^":
                    robot_vertical_position += 1
                elif element == "v":
                    robot_vertical_position -= 1
                elif element == ">":
                    robot_horizontal_position += 1
                elif element == "<":
                    robot_horizontal_position -= 1
                # Here integer position will be converted to string and receive a positive (+) or negative (-) clause for house identification
                if robot_vertical_position >= 0:
                    robot_vertical_string = "+" + str(abs(robot_vertical_position))
                else:
                    robot_vertical_string = "-" + str(abs(robot_vertical_position))

                if robot_horizontal_position >= 0:
                    robot_horizontal_string = "+" + str(abs(robot_horizontal_position))
                else:
                    robot_horizontal_string = "-" + str(abs(robot_horizontal_position))

                robot_current_position = str(robot_vertical_string) + str(robot_horizontal_string)
                print(f'Robot is at house number # {robot_current_position}')
                if robot_current_position not in robot_house_list:
                    robot_house_list.append(robot_current_position)
                current_deliver = "Santa"

    house_list = santa_house_list + robot_house_list
    house_list = list(dict.fromkeys(house_list))
    counter_delivered_houses = len(house_list)
    print(f'The total # of houses which received at least one presents = {counter_delivered_houses} ')