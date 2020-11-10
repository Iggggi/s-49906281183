w=4990628118300
s=0
d=0
a=0
p=1
print(a,d,p,s,w)
while w>0:
    c=w//10
    k=c+a+d
    s=s+(k//10)*p
    a=c
    p=p*10
    w=w//10
    print(a,d,p,s,w)
    if s==49906281183:
        print ('s=49906281183, w=',w)
s=s+(a+d)*p
print(s)