def linear(n):
    if n == 0 :
        return
    print(n, end=" ")
    linear(n - 1)

print("Linear Recursion (one call per level):")
linear(5)
print()

def tail(n):
    if n == 0:
        return
    print(n, end=" ")
    tail(n - 1)

print("Tail Recursion (prints going down):")
tail(5)
print()

def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n, end=" ")

print("Head Recursion (prints going up):")
head(5)
print()

def inc_dec(n):
    if n == 0:
        return
    print(n, end=" ")
    inc_dec(n - 1)
    print(n, end=" ")

print("Increment and Decrement Recursion (prints going down and up):")
inc_dec(4)
print()

def tree(n):
    if n == 0:
        return
    print(n, end=" ")
    tree(n - 1)
    tree(n - 1)

print("Tree Recursion (two calls per level):")
tree(3)
print()
print("Level calls: 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 128 -> 256 -> 512 -> 1024 -> 2048 -> 4096 -> 8192 -> 16384 -> 32768 -> 65536 -> 131072 -> 262144 -> 524288 -> 1048576")