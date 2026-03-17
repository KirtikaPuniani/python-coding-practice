# CI = P(1 + r/n)^nt
# n is no of times interest compounds per year

principal = float(input("please enter the initial amount: "))
rate = float(input("please enter the rate of interest per annum: "))
time = float(input("please enter the time period in years: "))
n = float(input("please enter the number of times interest is compounded per year: "))

Compound_Interest = principal * (1 + (rate/n)) ** (n*time)
print(Compound_Interest)