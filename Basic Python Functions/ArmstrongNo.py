# class ArmstrongNumber(object):
#     def armstrong(self, x):
#         n = len(str(x))
#         temp = x
#         total = 0

#         while x > 0:
#             digit = x % 10
#             total += digit ** n
#             x //= 10

#         return total == temp

# X = ArmstrongNumber()
# print(X.armstrong(1634))

num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")