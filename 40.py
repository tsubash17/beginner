x = input()
n1=0
n2=1
n3=0
for i  in range(0,x):
    c=n1+n2
    n1=n2
    n2=c
    print n1
