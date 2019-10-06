N=int(input())
list=[]
for _ in range(N):
    list.append(int(input()))
list=sorted(list)
for i in range(N):
    print(list[i])