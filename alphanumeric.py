a=input()
c=0
l=0
for b in a:
    if(b.isalpha()):
       c=c+1
    if(b.isdigit()):
        l=l+1
    if(c>1 and l>1):
        print "yes"
        break
else:
    print "no"
