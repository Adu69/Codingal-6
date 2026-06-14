def countdown(n):
    if n == 0:
        return
    print("counting down from 5")
    print(n,  end = "")
    countdown(n-1)

countdown(5)
