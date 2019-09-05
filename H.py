adress_list = []
bad_adress = []

n = int(input())
m = int(input())
k = int(input())

i = 0
while (i < n):
    ip_adress = str(input())
    adress_list.append(ip_adress)
    i += 1

for j in range(0, (len(adress_list)-m)+1):
    m += 1
    for lst in adress_list[j:m]:
        if adress_list[j:m].count(lst) >= k:
            if lst not in bad_adress:
                bad_adress.append(lst)

result_bad_lst = sorted(bad_adress)
for lst in result_bad_lst:
    print(lst)
