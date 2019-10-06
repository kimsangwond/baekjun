N=int(input())
total_list=[]
total_count=[]
rank=[]
count=-1
ranking=1
red=0

for _ in range(N):
    human=list(map(int, input().split()))
    total_list.append(human)
    total_count.append(0)
    rank.append(0)

for i in range(len(total_list)):
    count += 1
    for b in range(len(total_list)):
        if a[0] < total_list[b][0] and a[1] < total_list[b][1]:
            total_count[count] += 1

for i in range(N):
    print(total_count[i]+1, end=' ')


'''
for _ in range(N):
    human=list(map(int, input().split()))
    total_list.append(human)
    total_count.append(0)
    rank.append(0)

while len(total_list)>1:
    a=total_list.pop(0)
    count += 1
    for b in range(len(total_list)):
        if a[0]>total_list[b][0] and a[1]>total_list[b][1]:
            total_count[count] += 1
        elif a[0] < total_list[b][0] and a[1] < total_list[b][1]:
            total_count[count+b+1] += 1

while 1:
    max_num = max(total_count)
    if max_num == -1:
        break
    for i in range(N):
        if total_count[i]==max_num:
            rank[i]=ranking
            red +=1
            total_count[i]=-1
    ranking += red
    red=0


for i in range(N):
    print(rank[i], end=' ')
'''