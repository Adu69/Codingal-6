print("Reverse Lab")
print()
print()

n = int(input("Enter a number: "))
temp = n
while temp > 0:
    print("last digit:", temp % 10, ": remaining", temp // 10)
    temp = temp // 10
print()
print()
print()



def flipNumber(num):
    if num // 10 == 0:
        return num
    last = num% 10
    rest = flipNumber(num // 10)
    return last * (10 ** len(str(rest))) + rest

n2 = int(input("Enter number to flip: "))
print("Flipped number:", flipNumber(n2))
print()
print()
print()


def flipName(s):
    if len(s) == 1:
        return s
    return flipName(s[1:]) + s[0]
name = input("Enter name to flip: ")
print("Flipped name:", flipName(name))
print()
print()
print()

def isPower4(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return isPower4(n // 4)
    return False
print("Check if number is power of 4")
print()
num = int(input("Enter number: "))
if isPower4(num):
    print(num, "is a power of 4")
else:
    print(num, "is not a power of 4")
print()
print()
print()