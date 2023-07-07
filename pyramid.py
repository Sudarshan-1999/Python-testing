n = 5 

i, j = 1, 0
while(i<=n):
    while(j<=i-1):
        print("*", end=" ")
        j+=1
    print("\r")
    j=0;i+=1




def triangle(n):
    k = n -1