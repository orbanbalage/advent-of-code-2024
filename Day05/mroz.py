#
import math

#print("Hello World - Termux on Android")

rules = """47|53
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

rules_arr = []

for line in rules.split("\n"):
    #print(line.split("|"))
    rules_arr.append(line.split("|"))

#print(rules_arr)

pages = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

pages_arr = []

for line in pages.split("\n"):
    #print(line.split(","))
    pages_arr.append(line.split(","))

#print(pages_arr)

rule = [75,13]
page = [75,29,13]

def convert(lst):
    res_dict = {}
    for i in range(0, len(lst)):
        res_dict[lst[i]] = i
    return res_dict

page_dict = convert(page)
#print(page)
#print(page_dict)

def apply_rule(rule, page_dict):
   # if(page_dict[rule[0]] == 
   a = page_dict.get(rule[0], True)
   b = page_dict.get(rule[1], True)
   if(b < a):
       return False
   else:
       return True


#print(apply_rule(rule, page_dict)) #True
#print(apply_rule([75,13],{77: 0, 29: 1, 11: 2})) #True
#print(apply_rule([75,13],{77: 0, 29: 1, 13: 2})) #True
#print(apply_rule([75,13],{75: 0, 29: 1, 11: 2})) #True
#print(apply_rule([75,13],{75: 2, 29: 1, 13: 0})) #False

def sum_middle_page_nums(correct_pages):
    total = 0
    for page in correct_pages:
        #print(page[math.ceil(len(page)/2)-1])
        total += int(page[math.ceil(len(page)/2)-1])
    return total

print(sum_middle_page_nums(pages_arr))
        
