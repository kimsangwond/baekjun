S=input().upper()
find_alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' ,'L' ,'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
max=0

for i in find_alphabet:
    a= S.count(i)
    if a>max:
        max=a
        alphabet=i
    elif a==max:
        alphabet='?'

print(alphabet)