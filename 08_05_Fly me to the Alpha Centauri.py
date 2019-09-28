

if __name__ == '__main__':
    count = int(input())
    result_list=[]
    for i in range(count):
        x, y = map(int, input().split())
        distance = y-x
        result=calculate(distance)
        result_list.append(result)

    for i in result_list:
        print(i)


'''count=int(input())
x, y= map(int, input().split())
distance= y-x
n=1

while distance>=n*(n+1):
    n +=1
num=n-1

if (distance-num*(num+1))>num+1:
    print(num+2)
else:
    print(num+1)'''