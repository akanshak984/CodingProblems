# print all the prime numbers in range n
n = 100
A = []
for i in range(2,n+1):
    A.append(i)
L = []
i = 1
while (len(A)!=0):
    #print (A)
    while (i<len(A)):
        if (A[i]%A[0]==0):
            A.remove(A[i])
        i+=1
    L.append(A[0])
    A.remove(A[0])
    i = 1
print (L)