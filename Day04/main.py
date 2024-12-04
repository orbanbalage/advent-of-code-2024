# pyenv init 3.13.0

import numpy as np

with open("input") as input_file:
	input_text = input_file.read()

#print(input_text)
#print(len(input_text))	# OK it's not very big. no worries.

input_sample = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""


#print(input_sample)

# sample should return 18

# 8 ways, 8 functions?
# 4 functions, parameter = iterate +/- (also defined where we start, 1,1 coordinates, or n,n)
# 2 functions (straight vs. diagonal), parameter = which dimension to iterate first (x, y axis) - also defines where we start??
# straight is trivial
# diagonal - also trivial, just slower and more complex steps, but we iterate through all elements...

# oh actually it's easy - we only check for the word, if the element we're iterating on == "X", and then we check all the additional three conditionals for letters "MAS" 

input_sample2 = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

# sample 2 should return 9

#for line in input_sample:
#	print(line)

input_sample_width = input_sample.find("\n") #10
input_sample_height = input_sample.count("\n") + 1 #10
#print(input_sample_height)

input_width = input_text.find("\n")
input_height = input_text.count("\n")
print(input_width) #140
print(input_height) #1

input_arr = np.empty([input_height, input_width], dtype="U")
print(input_arr)

x, y = 0, 0

for line in input_text.split("\n"): #replace to input_sample or input_sample2 for testing...
	#print(line)
	for char in line:
		#print(char, x, y)
		input_arr[x][y] = char
		y += 1
	x += 1
	y = 0

print(input_arr)
#################

xmas_count = 0

#we can express each vector, like the clock. 3PM means horizontal, LTR.

# we can iterate just once!!!:
for x in range(0, input_height):
	for y in range(0, input_width):
		#print(input_arr[x][y])
# and write the conditions here for each clock:
# 3PM:
		if(y + 3 < input_width and input_arr[x][y] == "X" and input_arr[x][y+1] == "M" and input_arr[x][y+2] == "A" and input_arr[x][y+3] == "S"):
			xmas_count += 1	##201. regex says 212. hmm... ///OK FIXXED! //also for one line sample, it's 5.
# 9PM:
		if(y >= 3 and input_arr[x][y] == "X" and input_arr[x][y-1] == "M" and input_arr[x][y-2] == "A" and input_arr[x][y-3] == "S"):
			xmas_count += 1	## ? //for one line sample = 2 VERIFIED.
# 6PM:
		if(x + 3 < input_height and input_arr[x][y] == "X" and input_arr[x+1][y] == "M" and input_arr[x+2][y] == "A" and input_arr[x+3][y] == "S"):
			xmas_count += 1
#12PM:
		if(x >= 3 and input_arr[x][y] == "X" and input_arr[x-1][y] == "M" and input_arr[x-2][y] == "A" and input_arr[x-3][y] == "S"):
			xmas_count += 1
#4,5PM:
		if(x + 3 < input_height and y + 3 < input_width and input_arr[x][y] == "X" and input_arr[x+1][y+1] == "M" and input_arr[x+2][y+2] == "A" and input_arr[x+3][y+3] == "S"):
			xmas_count += 1
#10,5PM:
		if(y >= 3 and x >= 3 and input_arr[x][y] == "X" and input_arr[x-1][y-1] == "M" and input_arr[x-2][y-2] == "A" and input_arr[x-3][y-3] == "S"):
			xmas_count += 1
#7,5PM:
		if(x + 3 < input_height and y >= 3 and input_arr[x][y] == "X" and input_arr[x+1][y-1] == "M" and input_arr[x+2][y-2] == "A" and input_arr[x+3][y-3] == "S"):
			xmas_count += 1
#1,5PM:
		if(x >= 3 and y + 3 < input_width and input_arr[x][y] == "X" and input_arr[x-1][y+1] == "M" and input_arr[x-2][y+2] == "A" and input_arr[x-3][y+3] == "S"):
			xmas_count += 1


print(xmas_count)

#################

# M.S
# .A.
# M.S

# 4 combo. Counter-Clockwise from bottom right:

# 4,5 +  1,5	SSMM
# 7,5 +  4,5	SMMS
#10,5 +  7,5	MMSS
# 1,5 + 10,5	MSSM

mas_count = 0

#we can express each vector, like the clock. 3PM means horizontal, LTR.

# we can iterate just once!!!:
for x in range(0, input_height):
	for y in range(0, input_width):
		#print(input_arr[x][y])
# and write the conditions here for each clock:
#4,5PM:
		if(x + 1 < input_height and y + 1 < input_width and x - 1 >= 0 and y - 1 >= 0 and  input_arr[x][y] == "A" and input_arr[x+1][y+1] == "S" and input_arr[x-1][y+1] == "S" and input_arr[x-1][y-1] == "M" and input_arr[x+1][y-1] == "M"):
			mas_count += 1
#10,5PM:
		if(x + 1 < input_height and y + 1 < input_width and x - 1 >= 0 and y - 1 >= 0 and  input_arr[x][y] == "A" and input_arr[x+1][y+1] == "S" and input_arr[x-1][y+1] == "M" and input_arr[x-1][y-1] == "M" and input_arr[x+1][y-1] == "S"):
			mas_count += 1
#7,5PM:
		if(x + 1 < input_height and y + 1 < input_width and x - 1 >= 0 and y - 1 >= 0 and  input_arr[x][y] == "A" and input_arr[x+1][y+1] == "M" and input_arr[x-1][y+1] == "M" and input_arr[x-1][y-1] == "S" and input_arr[x+1][y-1] == "S"):
			mas_count += 1
#1,5PM:
		if(x + 1 < input_height and y + 1 < input_width and x - 1 >= 0 and y - 1 >= 0 and  input_arr[x][y] == "A" and input_arr[x+1][y+1] == "M" and input_arr[x-1][y+1] == "S" and input_arr[x-1][y-1] == "S" and input_arr[x+1][y-1] == "M"):
			mas_count += 1


print(mas_count)

