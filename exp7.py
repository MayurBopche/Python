n=int(input("Enter Number: "))
for i in range(0,n):
    for j in range(i,n):
        if i*i + j*j ==n:
            print([i,j])
