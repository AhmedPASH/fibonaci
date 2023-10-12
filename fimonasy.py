#Fibonacci series
n1=0
n2=1
n=int(input())
i=1
if n==1:
    print(n1)
else:
    print(n1,n2,end=" ")
    while i<n-1:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        i=i+1