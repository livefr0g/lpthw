def build_list(len, inc):
    i = 0
    numbers = []
    while i < len:
        print "At the top i is %d" % i
        numbers.append(i * inc)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

print "Enter length of list: ",
len = int(raw_input())
print "Enter incrementor value: ",
inc = int(raw_input())
num_list = build_list(len, inc)

print "The numbers: "

for num in num_list:
    print num