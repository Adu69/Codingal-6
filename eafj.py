a = int(input("enter the number you wish to count upto: "))
def count_up(n):
    if n > a:
        return
    print("n, end =")
    count_up(n+1)

print("Counting from 1 to 10 using recursion..")
print()
c = int(input("enter starting number: "))
print()
count_up(c)
