scores = [10, 20, 30, 40, 50]

def head_tail(lst):
    if len(lst) == 0:
        print("Empty list")
        return
    print("Head:", lst[0])
    print("Tail:", lst[1:])

head_tail(scores)
print()
print()
scores = [10, 20, 30, 40, 50]

def print_list(lst):
    if len(lst) == 0:
        return
    print(lst[0])
    print_list(lst[1:])

print_list(scores)
print()
print()
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_sorted(lst[1:])

if is_sorted(scores):
    print("Sorted")
else:
    print("Not Sorted")
print()
print()
scores = [10, 20, 30, 40, 50]

def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print("Sum =", recursive_sum(scores))

scores = [10, 20, 30, 40, 50]

def largest(lst):
    if len(lst) == 1:
        return lst[0]

    biggest = largest(lst[1:])

    if lst[0] > biggest:
        return lst[0]
    else:
        return biggest

print("Largest =", largest(scores))