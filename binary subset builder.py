items = ["A", "B", "C"]

n = len(items)

for mask in range(2 ** n):
    subset = []

    for i in range(n):
        if (mask >> i) & 1:
            subset.append(items[i])

    print(subset)