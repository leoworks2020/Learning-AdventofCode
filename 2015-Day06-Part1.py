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
Challenge Completion Day:   x
'''
#Puzzle Part I
# TODO: Create a matrix based on the size required
# TODO: Create vars to flag different actions: on, off, toggle
# TODO: Create if condition based on each different action

#Defining grid vars
grid = list
row = int
column = int

#Defining action vars
light_action = str
grid_action_start = list
grid_action_end = list
instruction = list

light_action = ""
grid_action_start = []
grid_action_end = []
instruction = []

#Mounting the Grid and Setting all lighs off
row = 6
column = 6
grid = [[column for column in range(column)] for row in range(row)]
for row in range(row):
    for column in range(column):
        grid[row][column] = 0
        column += 1
    row += 1
print(f'Starting the grid...')
print(grid)

#Executing instructions
with open("input/2015-Day06-input.txt") as f:
    print(f"---------------------------------")
    #Reading each line of the file
    instruction = f.readline()
    print(f'Executing the following instruction:')
    print(instruction)
    instruction = instruction.split(" ")

    #Normalizing list based on readline
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

    #row = 0
    #column = 0
    for row in range(grid_row_start,grid_row_end+1):
        for column in range(grid_column_start,grid_column_end+1):
            #print(f'Grid Row {row}{column} = {grid[row][column]}')
            #TODO: Create IFs for light action, but first refine action for "turn on" and "turn off"

            #Executing taking actions on each light on the grid
            print(f'Executing light instructions...')
            if light_action == "turn on":
                print(f'Turning on light: {row}{column}')
                grid[row][column] = 1
            if light_action == "turn off":
                print(f'Turning off light: {row}{column}')
                grid[row][column] = 0
            if light_action == "toggle":
                print(f'Toggling light: {row}{column}')
                if grid[row][column] == 0:
                    grid[row][column] = 1
                elif grid[row][column] == 1:
                    grid[row][column] = 0
            column += 1
        row += 1
        print(grid)
    print(f"Moving to the next instruction...")
    print(f"---------------------------------")