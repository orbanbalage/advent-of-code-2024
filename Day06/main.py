# numpy like Day04
import numpy

sample_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


with open("input.txt") as inputfile:
    puzzle = inputfile.read()


#print(puzzle.find("\n")) #130
#print(puzzle.count("\n")) #130

dims = puzzle.find("\n")
arr = numpy.empty([dims,dims], dtype="U")

x,y = 0,0

for line in puzzle.split("\n"):
    for char in line:
        arr[x][y] = char
        y += 1
    x += 1
    y = 0

print(arr)

