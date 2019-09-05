T1 = []
row1 = []

T2 = []
row2 = []

T3 = []
row3 = []

n1 = int(input()) # Количество строк в таблице T1
i = 0
while (i < n1):
    T1.append([int(i) for i in input().split()])
    i += 1

i = 0
n2 = int(input()) # Количество строк в таблице T2
while (i < n2):
    T2.append([int(i) for i in input().split()])
    i += 1

operation = str(input())

if operation == 'INNER':
    for i in range(len(T1)):
        if (T1[i][0] == T2[i][0]): # Если совпадают первые элементы строк - соединяем
            T3.append([T1[i][0], T1[i][1], T2[i][1]])

    print(len(T3))
    for lst in T3:
        for i in lst:
            print(i, end=' ')
        print()

if operation == 'LEFT':
    for i in range(len(T1)):
        if (T2[i][0] != T1[i][0]):
            T3.append([T1[i][0], T1[i][1], 'NULL'])
        elif (T1[i][0] == T2[i][0]):
            T3.append([T1[i][0], T1[i][1], T2[i][1]])
    print(len(T3))
    for lst in T3:
        for i in lst:
            print(i, end=' ')
        print()

if operation == 'RIGHT':
    for i in range(len(T2)):
        if (T2[i][0] != T1[i][0]):
            T3.append([T2[i][0], 'NULL', T2[i][1]])
        elif (T1[i][0] == T2[i][0]):
            T3.append([T2[i][0], T1[i][1], T2[i][1]])
    print(len(T3))
    for lst in T3:
        for i in lst:
            print(i, end=' ')
        print()

if operation == 'FULL':
    max_length = max(len(T1), len(T2))
    for i in range(max_length):
        if (T1[i][0] == T2[i][0]):
            T3.append([T1[i][0], T1[i][1], T2[i][1]])
        else:
            T3.append([T1[i][0], T1[i][1], 'NULL'])
            T3.append([T2[i][0], 'NULL', T2[i][1]])

    print(len(T3))
    for lst in T3:
        for i in lst:
            print(i, end=' ')
        print()
