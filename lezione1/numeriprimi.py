n=int(input('numero'))
l=[]
for i in range(1,n+1):
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
    if isprime==True:
        l.append(i)
print(l)