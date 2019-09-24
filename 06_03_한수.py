n=int(input())

def split(number):
    list=(([int(i) for i in str(number)]))
    print(list)
    return list

def classification(number, list, diff):
    for m in range(5):
        if number<(list[0]*100)+((list[0]+diff+m)*10)+(list[0]+2*(diff+m)):
            print(99+(list[0]-1)*5+m)
            break
        elif number>=(list[0]*100)+((list[0]+diff+4)*10)+(list[0]+2*(diff+4)):
            print(99+(list[0])*5)
            break

if __name__ == '__main__':
    split_number_list= split(n)

    if len(split_number_list)<3:
        print(n)

    elif n==1000:
        print(144)

    else:
        for i in range(4, -1, -1):
            print(i)
            if split_number_list[0]-2*i>=0:
                break
        classification(n, split_number_list, -i)

# 모범답안
'''
num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1 
    
    else :     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1
'''