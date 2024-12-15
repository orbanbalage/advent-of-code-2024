#
# pyevn versions
#* 3.13.0 (set by /Users/orbanbalage/.python-version)

# numpy like Day04

# python3 -m pip install numpy
# Requirement already satisfied: numpy in /Users/orbanbalage/.pyenv/versions/3.13.0/lib/python3.13/site-packages (2.1.3)

import numpy
import itertools

sample_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

sample_dims = sample_input.find("\n") # 12
sample_arr = numpy.empty([sample_dims,sample_dims], dtype="U")
sample_anti_arr = numpy.empty([sample_dims,sample_dims], dtype="U")

x,y = 0,0

for line in sample_input.split("\n"):
    for char in line:
        sample_arr[x][y] = char
        sample_anti_arr[x][y] = char
        y += 1
    x += 1
    y = 0

print(sample_arr)

sample_dict = {}
sample_comb_dict = {}

def build_dict(arr, x, y):
	if(arr[x][y] == "."):
		return
	if(sample_dict.get(arr[x][y]) == None):
		sample_dict[arr[x][y]] = []
	sample_dict[arr[x][y]].append((x,y))

for x in range(0, sample_arr.shape[0]):
	for y in range(0, sample_arr.shape[1]):
		build_dict(sample_arr, x, y)

print(sample_dict)

for char in sample_dict:
	#print(list(itertools.combinations(sample_dict[char], 2)))
	sample_comb_dict[char] = []
	sample_comb_dict[char] = list(itertools.combinations(sample_dict[char], 2))
	#for (x, y) in sample_dict[char]:
		#print(x, y)

print(sample_comb_dict)


def calc_nodes(p):
     x = p[0][0]
     y = p[0][1]
     z = p[1][0]
     zs = p[1][1]
     a = z - x
     b = zs - y
     return((x-a, y-b),(z+a, zs+b))


def write_nodes(p):
	x = p[0][0]
	y = p[0][1]
	z = p[1][0]
	zs = p[1][1]
	if(
		0 <= x < sample_dims
		and 0 <= y < sample_dims
	):
		sample_anti_arr[x][y] = "#"
	if(
		0 <= z < sample_dims
		and 0 <= zs < sample_dims
	):
		sample_anti_arr[z][zs] = "#"


for char in sample_comb_dict:
	for ((x, y), (z, zs)) in sample_comb_dict[char]:
		print(x, y, z, zs)
		print(calc_nodes(((x, y), (z, zs))))
		write_nodes(calc_nodes(((x, y), (z, zs))))


		
count_X = (sample_anti_arr == "#").sum()
print(count_X)

with open("input") as inputfile:
    puzzle = inputfile.read()


#print(puzzle.find("\n")) #50
#print(puzzle.count("\n")) #50

dims = puzzle.find("\n")
arr = numpy.empty([dims,dims], dtype="U")
anti_arr = numpy.empty([dims,dims], dtype="U")


x,y = 0,0

for line in puzzle.split("\n"):
    for char in line:
        arr[x][y] = char
        anti_arr[x][y] = char
        y += 1
    x += 1
    y = 0

#print(arr)

#import sys
#print(sys.getrecursionlimit()) #1000

#sys.setrecursionlimit(15000) #crazy?

adict = {}
comb_dict = {}


def build_dict(arr, x, y):
	if(arr[x][y] == "."):
		return
	if(adict.get(arr[x][y]) == None):
		adict[arr[x][y]] = []
	adict[arr[x][y]].append((x,y))

for x in range(0, arr.shape[0]):
	for y in range(0, arr.shape[1]):
		build_dict(arr, x, y)

print(adict)

for char in adict:
	#print(list(itertools.combinations(adict[char], 2)))
	comb_dict[char] = []
	comb_dict[char] = list(itertools.combinations(adict[char], 2))
	#for (x, y) in adict[char]:
		#print(x, y)

print(comb_dict)



def write_nodes(p):
	x = p[0][0]
	y = p[0][1]
	z = p[1][0]
	zs = p[1][1]
	if(
		0 <= x < dims
		and 0 <= y < dims
	):
		anti_arr[x][y] = "#"
	if(
		0 <= z < dims
		and 0 <= zs < dims
	):
		anti_arr[z][zs] = "#"



for char in comb_dict:
	for ((x, y), (z, zs)) in comb_dict[char]:
		print(x, y, z, zs)
		print(calc_nodes(((x, y), (z, zs))))
		write_nodes(calc_nodes(((x, y), (z, zs))))

count_X = (anti_arr == "#").sum()
print(count_X)
