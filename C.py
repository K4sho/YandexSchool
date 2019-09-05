n = int(input())
k = [int(i) for i in input().split()]

def rec(n):
    f_sum = 0
    f0 = 0
    f1 = 1
    f2 = 2
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        i = 0
        while i < n - 2:
            f_sum = f0 + f2
            f0 = f1
            f1 = f2
            f2 = f_sum
            i += 1
        return(f_sum)

for i in k:
    print(rec(i), end=" ")
