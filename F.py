from collections import Counter

n = int(input())

sessions = []
i = 0
while(i < n):
    s, f = input().split()
    s = int(s)
    f = int(f)
    sessions.append([i for i in range(s, f+1)])
    i += 1

out_list = [item for sublist in sessions for item in sublist]

count = Counter(out_list)
print(count.most_common()[0][0])

