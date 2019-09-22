n=input()
result_list=[]
for i in range(int(n)):
    ox_string=input()
    score, continuity=0, 0
    for y in ox_string:
        if y=='O':
            continuity += 1
        else:
            continuity = 0
        score += continuity
    result_list.append(score)

for pop in result_list:
    print(pop)