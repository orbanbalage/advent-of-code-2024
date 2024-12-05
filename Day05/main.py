# pyenv init 3.13.0

#import numpy as np

with open("input") as input_file:
	input_text = input_file.read()

#print(input_text.split("\n\n\n"))
#print(len(input_text))

rules_arr = []
pages_arr = []

i = 0
for block in input_text.split("\n\n"):
	if i == 0:
		for line in block.split("\n"):
			rules_arr.append(line.split("|"))
		i = 1
		#print(i, block)
	else:
		for line in block.split("\n"):
			pages_arr.append(line.split(","))

#print(rules_arr)
#print(pages_arr)

input_rules_sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""


input_pages_sample = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules_arr_sample = []
pages_arr_sample = []

for line in input_rules_sample.split("\n"):
	#print(line.split("|"))
    rules_arr_sample.append(line.split("|"))
   
#print(rules_arr_sample)


for line in input_pages_sample.split("\n"):
	#print(line.split("|"))
    pages_arr_sample.append(line.split(","))
   
#print(pages_arr_sample)


