import copy

test = [[1,2,3,4,5],[7,7,7,7]]
neo = []

print(test)
print(neo)

for i in range(0, len(test)):
	neo.append([])
	print("neo: ", neo)
	for j in range(0, len(test[i])):
		print("appending x times = ", len(test[i]))
		neo[i].append(test[i][:]) ##### BRUH - "slicing operation" was necessary... === [:]
	print(f"neo[{i}] is now ready: ", neo[i])

print("neo = ", neo)
# neo =  [[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7]]]

#neo2 = copy.deepcopy(neo)
for k in range(0, len(neo)):
	for l in range(0, len(neo[k])):
		print(f"neo: ", neo)
		#print(f"neo2: ", neo2)
		print(f"pop: neo{[k]}{[l]}{[l]}", neo[k][l][l])
		#print(f"pop: neo2{[k]}{[l]}{[l]}", neo2[k][l][l])
		neo[k][l].pop(l)
		#print(f"len(neo2): {len(neo2)}, k: {k}")
		#print(f"len(neo2[{k}]): {len(neo2[k])}, l: {l}")
# Note
# There is a subtlety when the sequence is being modified by the loop
# https://docs.python.org/3.9/reference/compound_stmts.html#the-for-statement



#for i in range(0, len(neo)):
#	for k in range(0, len(neo[i])):
#		print("i, k, neo[i][k][k] = ", i, k, neo[i][k][k])
#		print("i, k, neo[i][k] = ", i, k, neo[i][k])
#		neo[i][k].pop(k)
#		print(f"neo[{i}][{k}]: ", neo[i][k])
#		print(f"neo[{i}]: ", neo[i])
#		print(f"neo: ", neo)

print("neo cut down = ", neo)
