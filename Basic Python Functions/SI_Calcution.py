# principal = int(input("please enter the initial amount: "))
# rate = int(input("please enter the rate of interest per annum: "))
# time = int(input("please enter the time period in years: "))

# Simple_Interest = (principal * rate * time) / 100
# print(Simple_Interest)

# #using function
# def simple_interest(p,r,t):
#     SI = (p * r * t) / 100
#     return SI

# SI = simple_interest(10000,3,1)
# print(SI)

#using lambda
Simple_Interest = lambda p,r,t: (p*r*t)/100
p,r,t = 10000, 3, 1
SI = Simple_Interest(p,r,t)
print(SI)