num_list=input().split(' ')
num1, num2 ='', ''

for i in num_list[0]:
    num1= i + num1

for i in num_list[1]:
    num2= i + num2

print(max(num1, num2))