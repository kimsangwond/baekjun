n=int(input())
i=2

if n==1:
    print(1)
else:
    while n>=2+3*(i-1)*(i-2):
        i += 1
    print(i-1)