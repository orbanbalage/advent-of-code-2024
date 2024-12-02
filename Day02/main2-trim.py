
test = [[1,2,3,4,5],[7,7,7,7],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1]]


def generate_removed_levels(input_list):
	new_list = []
	for i in range(0, len(input_list)):
		new_list.append([])
		for j in range(0, len(input_list[i])):
			new_list[i].append(input_list[i][:]) ##### BRUH - "slicing operation" was necessary... === [:]
	
	for k in range(0, len(new_list)):
		for l in range(0, len(new_list[k])):
			new_list[k][l].pop(l)
	return new_list

neo = generate_removed_levels(test)
print(neo)
