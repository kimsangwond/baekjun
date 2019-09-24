n=int(input())
hell=n
arr=[["*"]*n for _ in range(n)]
count=2

while n // 3 != 3:
    n = n // 3
    count += 1

for i in range(count):
    for a in range(hell):
        if (a // 3 ** i) % 3 == 1:
            for z in range(hell):
                if (z // 3 ** i) % 3 == 1:
                        arr[a][z] = ' '

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))


'''
for i in range(hell):
    for a in range(hell):
        print(arr[i][a], end='')
    print()
'''





'''
n=int(input())
hell=n
arr=[["*"]*n for _ in range(n)]
count=2

if __name__ == '__main__':

    while n // 3 != 3:
        n = n // 3
        count += 1

    for i in range(count):
        for a in range(hell):
            if (a // 3 ** i) % 3 == 1:
                for z in range(hell):
                    if (z // 3 ** i) % 3 == 1:
                        arr[a][z] = ' '

    for i in range(hell):
        for z in range(hell):
            print(arr[i][z], end='')
        print()
'''