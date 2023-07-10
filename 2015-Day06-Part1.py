'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day06-Part1
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-07
Challenge Completion Day:   2023-07-10
'''
#Puzzle Part I
# DONE: Create a matrix based on the size required
# DONE: Create vars to flag different actions: on, off, toggle
# DONE: Create if condition based on each different actions

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
total_lit_lights = int

light_action = ""
grid_action_start = []
grid_action_end = []
instruction = []
instruction_number = 0
total_lit_lights = 0

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
                    grid[row][column] = 1
                if light_action == "turn off":
                    #[DEBUG ONLY] print(f'Turning off light: {row}{column}')
                    grid[row][column] = 0
                if light_action == "toggle":
                    #[DEBUG ONLY]print(f'Toggling light: {row}{column}')
                    if grid[row][column] == 0:
                        grid[row][column] = 1
                    elif grid[row][column] == 1:
                        grid[row][column] = 0
                column += 1
            column = grid_column_start
            row += 1
        print(f"Moving to the next instruction...")
        print(f"---------------------------------")
print(f"End of processing.")

#Counting number of lights that are lit
row = 999
column = 999
for row in range(0,row + 1):
    if row == len(grid):
        break
    for column in range(0,column + 1):
        if column == len(grid):
            break
        if grid[row][column] == 1:
            total_lit_lights += 1
        column += 1
    row += 1
print(f"The total number of lights lit are: {total_lit_lights}")
