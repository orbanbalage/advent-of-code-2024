#vim - how to yank all lines:
#ESC gg 
#"*y
#G

list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

list1.sort()
list2.sort()

tuples = zip(list1, list2)

#ZIP is destroyed after use!
#print(list(tuples))

result = 0

for x,y in tuples:
    #print(tuples[i][0], tuples[i][1])
    #print(abs(x-y))
    result += abs(x-y)

print(result)

#re-create this as a function

def zip_and_sum_diffs(list1, list2):
	list1.sort()
	list2.sort()
	tuples = zip(list1, list2)
	result = 0
	for x,y in tuples:
		result += abs(int(y)-int(x))
	return result

#test function on sample data
test_result = zip_and_sum_diffs(list1, list2)
print(test_result) #should return 11!

#we need to parse the puzzle input that's much longer
#let's create a short sample of it:
sample_input = """31594   93577
46608   24099
78052   70524"""

lines = sample_input.splitlines()
#lines.remove("")
print(lines)

total_diff = 0

for line in lines:
    print(line.split("   "))
    x, y = line.split("   ")
    #print(x, y)
    print(abs(int(y)-int(x)))
    total_diff += abs(int(y)-int(x))
    print(total_diff)


#let's turn this into a function
#so zipping two lists won't be needed...
#I'm an idiot, forgot to sort the lists...

def calculate_total_distance_between_lists(puzzle_input):
	lines = puzzle_input.splitlines()
	#lines.remove("")

	#total_diff = 0
	list1, list2 = [], []

	for line in lines:
		x, y = line.split("   ")
		list1.append(x)
		list2.append(y)
	#	total_diff += abs(int(y)-int(x))
	#return total_diff
	list1.sort()
	list2.sort()
	return zip_and_sum_diffs(list1, list2)

#test with our sample data
test_result2 = calculate_total_distance_between_lists(sample_input)
print(test_result2) #should be around 92k

#open the sample input from file and calculate the result
sample_file = open("sample_input")
sample_file_content = sample_file.read()
sample_file.close()

#let's see what we have read:
print("Sample File content what we have read:")
print(sample_file_content)

#do the thing:
print("Sample result reading - result should be 11", sample_file)
sample_final_result = calculate_total_distance_between_lists(sample_file_content)
print(sample_final_result) #11?




#open the input from file and calculate the result
file = open("input.txt")
file_content = file.read()
file.close()

#let's see what we have read:
#print("File content what we have read:")
#print(file_content)

#do the thing:
print("Final result reading ", file)
final_result = calculate_total_distance_between_lists(file_content)
print(final_result)
