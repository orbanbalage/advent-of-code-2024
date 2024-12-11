#
# pyevn versions
#* 3.13.0 (set by /Users/orbanbalage/.python-version)

# numpy like Day04

# python3 -m pip install numpy
# Requirement already satisfied: numpy in /Users/orbanbalage/.pyenv/versions/3.13.0/lib/python3.13/site-packages (2.1.3)

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


sample_dims = sample_input.find("\n") # 10
sample_arr = numpy.empty([sample_dims,sample_dims], dtype="U")

x,y = 0,0

for line in sample_input.split("\n"):
    for char in line:
        sample_arr[x][y] = char
        y += 1
    x += 1
    y = 0

print(sample_arr)

pos1, pos2 = numpy.where(sample_arr == "^")
print(pos1, pos2) # 6, 4

def up(arr, x, y):
	arr[x][y] = "X"
	#print(arr, x, y)
	#print(arr[x][y]) #IndexError: index 4 is out of bounds for axis 0 with size 1
	if(x == 0):
		print("End of Map")
		return
	if(arr[x-1][y] == "#"):
		right(arr, x, y)
	else:
		up(arr, x-1, y)

def right(arr, x, y):
	arr[x][y] = "X"
	if(y == arr.shape[1]-1):
		print("End of Map")
		return
	if(arr[x][y+1] == "#"):
		down(arr, x, y)
	else:
		right(arr, x, y+1)

def down(arr, x, y):
	arr[x][y] = "X"
	if(x == arr.shape[0]-1):
		print("End of Map")
		return
	if(arr[x+1][y] == "#"):
		left(arr, x, y)
	else:
		down(arr, x+1, y)

def left(arr, x, y):
	arr[x][y] = "X"
	if(y == 0):
		print("End of Map")
		return
	if(arr[x][y-1] == "#"):
		up(arr, x, y)
	else:
		left(arr, x, y-1)

#let's run this beast:
up(sample_arr, pos1[0], pos2[0])

count_X = (sample_arr == "X").sum()
print(count_X)

with open("input") as inputfile:
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

#print(arr)

pos1, pos2 = numpy.where(arr == "^")
print(pos1, pos2) # 48, 85

import sys
print(sys.getrecursionlimit()) #1000

sys.setrecursionlimit(15000) #crazy?

#let's run this beast:
up(arr, pos1[0], pos2[0])

# RecursionError: maximum recursion depth exceeded #FUUU

count_X = (arr == "X").sum()
print(count_X)
