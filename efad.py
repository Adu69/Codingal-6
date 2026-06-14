import sys
print("Python recursion limit: ", sys.getrecursionlimit(),"calls")

def nobasecase(n):
    print("Call", n, end ="")
    nobasecase(n+1)

sys.setrecursionlimit(30)
try:
    nobasecase(1)
except RecursionError:
    print()
    print("stack overflow!, no base case")

sys.setrecursionlimit(1000)
