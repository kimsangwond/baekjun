S=input()
croatia_alp=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
start_list=[]
count=0

for i in croatia_alp:
    while S.find(i)!= -1:
        S = S.replace(i, " ", 1)
        count = count+1

S= S.replace(" ", "")
count=len(S) + count
print(count)