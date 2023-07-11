'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day06-Part2
--- Day 6: Probably a Fire Hazard ---
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-11
Challenge Completion Day:   2023-07-11
'''
#Puzzle Part I
# DONE: Create a matrix based on the size required
# DONE: Create vars to flag different actions: on, off, toggle
# DONE: Create if condition based on each different actions
#Puzzle Part II
# DONE: Change values in lights from 0-1 to 0-n based on the increment given by the instruction
# DONE: Do a sanity check to make sure light value is never < 0
# DONE: At the end calculate the sum of values on each light as a grand total for the brightness


#Defining grid vars
grid = list
row = int
column = int

#Defining action vars
light_action = str
grid_action_start = list
grid_action_end = list
instruction = list
instruction_number = int
total_brightness_of_lit_lights = int

light_action = ""
grid_action_start = []
grid_action_end = []
instruction = []
instruction_number = 0
total_brightness_of_lit_lights = 0

#Mounting the Grid and Setting all lighs off
row = 999
column = 999
grid = [[column for column in range(column+1)] for row in range(row+1)]
for row in range(0,row + 1):
    if row >= len(grid):
        break
    for column in range(0,column + 1):
        if column >= len(grid):
            break
        grid[row][column] = 0
        column += 1
    row += 1
print(f'Starting the grid...')
print(grid)

#Executing instructions

#Resetting row and column values to zero
row = 0
column = 0
with open("input/2015-Day06-input.txt") as f:
    while True:
        #Reading each line of the file
        instruction = f.readline().strip()
        instruction_number += 1
        if not instruction:
            break

        instruction = list(instruction.split(" "))
        print(f'Executing instruction #{instruction_number}:')
        print(instruction)

        #Normalizing the list based on instruction in readline
        if instruction[0] == "turn" and instruction[1] == "on":
            instruction[0] = "turn on"
            instruction.pop(1)
        if instruction[0] == "turn" and instruction[1] == "off":
            instruction[0] = "turn off"
            instruction.pop(1)

        #Normalizing grid instructions
        light_action = instruction[0]
        grid_action_start = instruction[1].split(",")
        grid_action_end = instruction[3].split(",")
        grid_row_start = int(grid_action_start[0])
        grid_row_end = int(grid_action_end[0])
        grid_column_start = int(grid_action_start[1])
        grid_column_end = int(grid_action_end[1])

        row = 0
        column = 0
        for row in range(grid_row_start,grid_row_end+1):
            if row > grid_row_end+1:
                break
            for column in range(grid_column_start,grid_column_end+1):
                if column > grid_column_end+1:
                    break

                #Taking actions on each light on the grid
                #[DEBUG ONLY] print(f'Executing light instructions...')
                if light_action == "turn on":
                    #[DEBUG ONLY] print(f'Turning on light: {row}{column}')
                    grid[row][column] += 1
                if light_action == "turn off":
                    #[DEBUG ONLY] print(f'Turning off light: {row}{column}')
                    if grid[row][column] > 0:
                        grid[row][column] -= 1
                if light_action == "toggle":
                    #[DEBUG ONLY]print(f'Toggling light: {row}{column}')
                    grid[row][column] += 2
                column += 1
            column = grid_column_start
            row += 1
        print(f"Moving to the next instruction...")
        print(f"---------------------------------")
print(f"End of processing.")

#Counting total amount of brighness in all lights that are lit
row = 999
column = 999
for row in range(0,row + 1):
    if row == len(grid):
        break
    for column in range(0,column + 1):
        if column == len(grid):
            break
        total_brightness_of_lit_lights += grid[row][column]
        column += 1
    row += 1
print(f"The total amount of brightness in all lights that are lit = {total_brightness_of_lit_lights}")
