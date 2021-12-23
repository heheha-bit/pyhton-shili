
for i in range (1 , 10):
    for j in range(1 , i+1):
        ji = i * j
        print("%d*%d=%d"%(i,j,ji),end=" | ")

    print()