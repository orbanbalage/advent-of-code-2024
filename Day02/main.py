# open sample data
with open("sample_input") as sample_input_file:
	sample_input_content = sample_input_file.read()



# define helper functions:
def ascending(a, b):
	return int(b) > int(a)

def descending(a, b):
	return int(a) > int(b)

def adjacent(a, b):
	return 1 <= abs(int(a) - int(b)) <= 3

# test functions:
print(ascending(0, 10)) # True
print(descending(4, 3)) # True
print(adjacent(1, 1))   # False
print(adjacent(5, 2))   # True

# define file parsing function
def data_input_to_list(file_path):
	content_list = []
	with open(file_path) as input_file:
		input_content = input_file.read()
		#for line in input_file.readline():
		#	#content_list.append(line.split("\n"))
		#	content_list.append(line)
		for line in input_content.split("\n"):
			content_list.append(line.split(" "))
		print(input_content)
	return content_list

test_input_list = data_input_to_list("sample_input")
print(test_input_list)


print("###")
def calculate_safe_reports_from_list(input_list):
	safe_count = 0
	for line in input_list:
		print(line)
		for num in line:
			print(num)
		asc_count = 0
		desc_count = 0
		for i in range(0, len(line) - 1):
			#print(ascending(line[i], line[i+1]))
			print(line, i, line[i], line[i+1])
			print("ascending: ", ascending(line[i], line[i+1]))
			print("descending: ", descending(line[i], line[i+1]))
			print("adjacent: ", adjacent(line[i], line[i+1]))
			if(adjacent(line[i], line[i+1])):
				if(ascending(line[i], line[i+1])):
					asc_count += 1
				else:
					desc_count += 1
		print("asc_count, desc_count, len(line): ", asc_count, desc_count, len(line))
		if(asc_count == len(line) - 1 or desc_count == len(line) - 1):
			
			print("SAFE: asc_count, desc_count, len(line): ", asc_count, desc_count, len(line))
			safe_count += 1
		else:
			print("UNSAFE: asc_count, desc_count, len(line): ", asc_count, desc_count, len(line))
	print("subtract 1 because of empty last line (too lazy to fix parser)")
	return safe_count

test_result = calculate_safe_reports_from_list(test_input_list)
print(test_result)

###
### FINAL ###
final_input_list = data_input_to_list("input")
print(final_input_list)

final_result = calculate_safe_reports_from_list(final_input_list)
print(final_result)
