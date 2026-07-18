def extract_digits(n):
    if n == 0:
        return
    extract_digits(n // 10)
    print(n % 10)

num = int(input("Enter a number: "))
extract_digits(num)
print()
print()
def reverse_number(n, rev):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num, 0))
print()
print()
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
print()
print()
def is_power_of_4(n):
    if n == 1:
        return True
    if n <= 0 or n % 4 != 0:
        return False
    return is_power_of_4(n // 4)

num = int(input("Enter a number: "))

if is_power_of_4(num):
    print("Power of 4")
else:
    print("Not a power of 4")
