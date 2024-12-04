import re

#p1 = re.compile("/(mul\(\d{1,3},\d{1,3}\))/g")
#p2 = re.compile("/(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))/g")

#p1 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)"gm)
#p2 = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"gm)

p1 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)", re.MULTILINE | re.DOTALL)
p2 = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", re.MULTILINE | re.DOTALL)

parsed_string1="""mul(15,833)
mul(452,37)
mul(661,869)"""

parsed_string2="""},;who()^>',mul(594,203)~  ~*$'*select()mul(693,99)*>&()+{%{mul(225,584)when()why()#]}&mul(287,918)<from(332,448)<^:mul(296,804)'@why()'when(),do()(+%:(who(309,257)mul(402,955):-')]</how()'{mul(462,541)who()^'{]-mul(677,297):*)-)]mul(997,185)mul(159,913);where()'+>}^mul(368,284)!>mul(943,865){who() /mul(482,561)don't()<,}>what()why();why()mul(407,849)@-mul(516,359))%:*<~&,}from()do()how()^+#^]when()%why()mul(604,810)when()from()mul(688,243)< ?[-]-who()mul(321,988)<:(%~!"""

#re.findall(pattern, string)

with open("input") as input_file:
	input_file_content = input_file.read()

#print(input_file_content)

print("Part One")
print(parsed_string1)
print("Result: ")
print(p1.findall(parsed_string1))
#part1_tuples = p1.findall(parsed_string1)
part1_tuples = p1.findall(input_file_content)

print("Part Two")
print(parsed_string2)
print("Result: ")
print(p2.findall(parsed_string2))
#part2_tuples = p2.findall(parsed_string2)
part2_tuples = p2.findall(input_file_content)

# returns an array of tuples containing the number of elements / the pattern matched

#[('15', '833'), ('452', '37'), ('661', '869')]
part1_result = 0
for pair in part1_tuples:
	#print(pair)
	part1_result += int(pair[0]) * int(pair[1])

print("Part One Result is: ")
print(part1_result)

#'mul(594,203)'
def calc_mul_result(mul_string):
	nums = mul_string.replace("mul(","").replace(")","").split(",")
	return (int(nums[0]) * int(nums[1]))

#[('mul(594,203)', '', ''), ('mul(693,99)', '', ''), ('mul(225,584)', '', ''), ('mul(287,918)', '', ''), ('mul(296,804)', '', ''), ('', 'do()', ''), ('mul(402,955)', '', ''), ('mul(462,541)', '', ''), ('mul(677,297)', '', ''), ('mul(997,185)', '', ''), ('mul(159,913)', '', ''), ('mul(368,284)', '', ''), ('mul(943,865)', '', ''), ('mul(482,561)', '', ''), ('', '', "don't()"), ('mul(407,849)', '', ''), ('mul(516,359)', '', ''), ('', 'do()', ''), ('mul(604,810)', '', ''), ('mul(688,243)', '', ''), ('mul(321,988)', '', '')]
part2_result = 0
calc = True
for triple in part2_tuples:
	#print(triple)
	if(triple[0] and calc):
		part2_result += calc_mul_result(triple[0])
	elif(triple[1]):
		calc = True
	elif(triple[2]):
		calc = False

print("Part Two Result is: ")
print(part2_result)

