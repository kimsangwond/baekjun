data_list=input().split()
after_data=list(map(int,data_list))

if after_data[1]>=after_data[2]:
    print(-1)
else:
    ans= after_data[0]//(after_data[2]-after_data[1])+1
    print(ans)