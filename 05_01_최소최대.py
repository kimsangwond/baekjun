n=input()
input_numbers=input().split()
compare_lists=list(map(int,input_numbers))
print(min(compare_lists), end=' ')
print(max(compare_lists))