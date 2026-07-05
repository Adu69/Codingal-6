def head(n):
    if n == 0:
        return 0
    head(n - 1)
    print(n)
n1 = int(input("Enter a number: "))
head(n1)
print()
def tail(n):
    if n == 0:
        return 0
    print(n)
    tail(n - 1)
print()
n2 = int(input("Enter a number: "))
tail(n2)
print()
def linear(n):
    if n == 0:
        return 0
    linear(n-1)
    print(n)
n3 = int(input("Enter a number: "))
linear(n3)
print()
def tree(n):
    if n == 0:
        return 0
    tree(n-1)
    print(n)
    tree(n-1)
n4 = int(input("Enter a number: "))
tree(n4)
print()
def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n - 1)
    print(factorial(n))

n = int(input("Enter a number: "))
factorial(n)