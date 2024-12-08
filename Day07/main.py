
line1 = "190: 10 19"
line2 = "8751: 9 12 81 3"
line3 = "8750: 9 12 81 3"

puzzle = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

result = 0

def add(target, a, lst):
    if(len(lst) == 0):
        return target, a
    #print(a, " + ", lst[0], " :: ", lst[1:])
    return eval_equation(target, a + lst[0], lst[1:])


def multiply(target, a, lst):
    if(len(lst) == 0):
        return target, a
    #print(a, " * ", lst[0], " :: ", lst[1:])
    return eval_equation(target, a * lst[0], lst[1:])


def parse_line(line):
    res = line.split(": ")
    #print(res)
    target = int(res[0])
    rest = res[1]
    nums = []
    for num in rest.split(" "):
        nums.append(int(num))
    return target, nums

target, nums = parse_line(line2)

def eval_equation(target, subtotal, nums):
    add(target, subtotal, nums)
    multiply(target, subtotal, nums)
        #print("nums len: ", len(nums))
    #return 667 # this is weird
    if(len(nums) == 0):
        #print(target, " ?== ", subtotal)
        if(target == subtotal):
            print(target)
            return target
        else:
            return 0

#line_res = eval_equation(target, nums[0], nums[1:])
#print(line_res)

#for line in puzzle.split("\n"):
#    target, nums = parse_line(line)
#    eval_equation(target, nums[0], nums[1:])

with open("input") as file:
    puzzle = file.read()
    for line in puzzle.split("\n"):
        if(len(line) > 0):
            target, nums = parse_line(line)
            eval_equation(target, nums[0], nums[1:])
