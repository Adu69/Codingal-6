def count_up(n):
    if n > 10:
        return
    print(n, end ="")
    count_up(n-1)

print("Counting from 1 to 10 using recursion..")

count_up(1)
