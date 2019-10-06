N, M = map(int, input().split())
input_list=list(map(int, input().split()))
input_list=sorted(input_list, reverse=True)
final=0

while len(input_list)>2:
    a=input_list.pop(0)
    for i in range(len(input_list)):
        b=input_list[i]
        for c in input_list[i+1:]:
            sum=a+b+c
            if M-sum<M-final and sum<=M:
                final=sum

print(final)