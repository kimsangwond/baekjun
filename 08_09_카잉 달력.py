def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

def lcm(a, b):
    return a*b//gcd(a,b)

def calculate(M, N, x, y):
    last_num=lcm(M,N)
    y_list=[]

    while y <= last_num:
        y_list.append(y)
        y = y + N

    while x<=last_num:
        if x in y_list:
            return x
        else:
            x = x + M
            continue

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        M, N, x, y= map(int,input().split())
        result=calculate(M,N,x,y)
        if result == None:
            result= -1
        print(result)


'''
            while y <= last_num:
                y_list.append(y)
                y = y + N
'''


'''
    for x_fac in x_list:
        #a= y_list.index(x_fac)
        if x_fac in y_list:
            return x_fac
        else:
            continue
'''