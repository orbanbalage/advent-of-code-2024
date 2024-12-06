#

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

print(rules_arr)

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

print(pages_arr)
