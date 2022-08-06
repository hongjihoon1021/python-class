count=0
for i in range(200,801999909,1):
    if i%5 != 0:
        print(i,end=' ')
        count+=1
    if count==10:
        print()
        count=0
