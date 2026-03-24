class ArmstrongNumber(object):
    def armstrong(self, x):
        n = len(str(x))
        temp = x
        total = 0

        while x > 0:
            digit = x % 10
            total += digit ** n
            x //= 10

        return total == temp

X = ArmstrongNumber()
print(X.armstrong(1634))