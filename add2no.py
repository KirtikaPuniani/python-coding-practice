# a = int(input("please give the first number: "))
# b = int(input("please give the second number: "))

# c = a+b
# print(c)


def add(a,b):
    return a+b

sum = add(46568,67434)
print(sum)

#using lambda
sum = lambda a, b: a+b
print(sum(46568,67434))