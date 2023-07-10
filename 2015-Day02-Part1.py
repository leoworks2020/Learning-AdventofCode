'''
Objective: Resolve Coding Puzzles
'''

'''
Puzzle 2025-Day02
Puzzle Description:
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
--------------------------------------------------------------------------------
Challenge Start Day:        2023-07-04
Challenge Completion Day:   2023-07-04
'''
#Puzzle Part I
present_counter = int
present_lengh = int
present_width = int
present_heigh = int
paper_size_required = int
extra_paper_required = int
total_size_required = int
present_counter = 0
present_lengh = 0
present_width = 0
present_heigh = 0
paper_size_required = 0
total_size_required = 0

#Reading Input File and Extracting Present size
with open("input/2015-Day02-input.txt") as f:
    while True:
        present_counter += 1
        f_line = f.readline()
        f_line_split = f_line.split("x")
        if not f_line:
            break
        present_lengh = int(f_line_split[0])
        present_width = int(f_line_split[1])
        present_heigh = int(f_line_split[2])
        extra_paper_required = min(present_lengh*present_width,present_width*present_heigh,present_lengh*present_heigh)
        paper_size_required = ((2*present_lengh*present_width) + (2*present_width*present_heigh) + (2*present_heigh*present_lengh)) + extra_paper_required
        total_size_required += paper_size_required
        #TEST: print(f'{present_lengh}x{present_width}x{present_heigh}')
        print(f'Present number {present_counter} requires a paper of this size: {paper_size_required} square feet')
        print(f'Total paper required is now {total_size_required} square feeet')


#Puzzle Part II
present_ribbon_required = int
present_ribbon_required = 0
