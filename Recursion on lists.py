scores = [340, 120, 410, 85, 270, 190, 55]

print("=== PART 1: HEAD TAIL PATTERN ===")
print("Full leaderboard:        :", scores)
print("Head (scores[0]).       : ", scores[0])
print("Tail (scores[1:]).      : ", scores[1:])
print("Head of tail             :", scores[1:][0])
print("Tail of tail             :", scores[1:][1:])

def show_shrink(a, depth = 0):
    indent = "  " * depth
    print(f"{indent}List: {a}. -> length = {len(a)}")
    if len(a) == 1:
        print(f"{indent}Base case reached. Returning {a[0]}.")
        return a[0]
    show_shrink(a[1:], depth + 1)

print("\n=== PART 2: BASE CASE FOR LISTS ===")
show_shrink([410, 270, 190, 55])

def is_sorted(a):

    if len(a) <= 1:
        return True
    
    return a[0] <= a[1] and is_sorted(a[1:])

print("\n PART 3: SORTED CHECK")
print("Scores         :", scores)
print("Is sorted?     :", is_sorted(scores))

ranked = [55, 85, 120, 190, 270, 340, 410]
print("Ranked scores  :", ranked)
print("Is sorted?     :", is_sorted(ranked))

def total_score(a):
    if len(a) == 1:
        return a[0]
    return a[0] + total_score(a[1:])

print("\n PART 4: TOTAL SCORE")
print("Scores         :", scores)
print("Total score    :", total_score(scores))

def top_score(a):
    if len(a) == 1:
        return a[0]
    return max(a[0], top_score(a[1:]))

print("\n PART 5: LARGEST ELEMENT")
print("Scores         :", scores)
champ = top_score(scores)
print("Champs score    :", champ)
print("Champion is player :", scores.index(champ) + 1)