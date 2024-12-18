



def map_to_block(disk_map):
	file = True
	res = []
	file_num = 0
	for i in disk_map:
		# WTF, this was not in the rule!
		#if(file_num == 10):
		#	file_num = 0
		# OK misunderstood. treat multi-digit numbers as one.
		if(file):
			#append i times file_num
			for j in range(0, int(i)):
				res.append(str(file_num))
			file_num += 1
		else:
			#append i times "."
			for j in range(0, int(i)):
				res.append(".")
		file = not file
	#print(res)
	return res



test1 = "12345"
res1 = "0..111....22222"
assert(map_to_block(test1) == list(res1))

test2 = "2333133121414131402"
res2 = "00...111...2...333.44.5555.6666.777.888899"
assert(map_to_block(test2) == list(res2))

test3 = "1010101010101010101010"
res3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
assert(map_to_block(test3) == res3)

def defrag(map_res):
	res = []
	x = 0
	y = len(map_res) - 1
	for i in range(0, len(map_res)):
		if(x > y):
			break
	#while x <= y:
		if(map_res[x] != "."):
			res.append(map_res[x])
			x += 1
		elif(map_res[y] == "."):
			y -= 1
		elif(map_res[x] == "." and map_res[y] != "."):
			res.append(map_res[y])
			x += 1
			y -= 1
	#print(res)
	return(res)


#defrag1 = "022111222......"
defrag1 = "022111222"
#print(defrag1)
assert(defrag(res1) == list(defrag1))

#defrag2 = "0099811188827773336446555566.............."
defrag2 = "0099811188827773336446555566"
#print(defrag2)
assert(defrag(res2) == list(defrag2))

defrag3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#print(defrag3)
assert(defrag(res3) == defrag3)

def checksum(defr):
	res = 0
	for i in range(0, len(defr)):
		res += i * int(defr[i])
	#print(res)
	return(res)


sum1 = 60 # 0+2+4+3+4+5+12+14+16
print(sum1)
assert(checksum(defrag1) == sum1)
assert(checksum(defrag(map_to_block(test1))) == sum1)

sum2 = 1928
print(sum2)
assert(checksum(defrag2) == sum2)
assert(checksum(defrag(map_to_block(test2))) == sum2)

sum3 = 385
print(sum3)
assert(checksum(defrag3) == sum3)
assert(checksum(defrag(map_to_block(test3))) == sum3)


#ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 19999 digits; use sys.set_int_max_str_digits() to increase the limit

import sys
sys.set_int_max_str_digits(20000)

import time


with open("input") as file:
	final_input = file.read().split("\n")
#print(final_input[0])

start_time = time.time()
print(checksum(defrag(map_to_block(final_input[0]))))

#print(map_to_block(final_input[0]))
#print(defrag(map_to_block(final_input[0])))
#print(checksum(defrag(map_to_block(final_input[0]))))
# 89859464970123 == TOO HIGH!
# 898594649709 == not right
# 89859464970 == TOO LOW!
# 5602261504 == TOO LOW!
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
