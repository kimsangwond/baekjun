def calculate(H, W, N):

    if H*W==N:
        num=str(W)
        floor=str(H)
    elif N%H==0:
        num=str(N//H)
        floor=str(H)
    else:
        num=str((N//H)+1)
        floor=str(N%H)

    if len(num)==1:
        num=('0'+num)
    res=floor+num
    return res


if __name__ == '__main__':
    count = int(input())
    result_list=[]
    for i in range(count):
        Height, Width, Number = map(int, input().split())
        result=calculate(Height, Width, Number)
        print(int(result))