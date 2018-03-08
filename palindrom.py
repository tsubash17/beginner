c=input()
temp=c

rev=0

while c>0:

    b=c%10

    rev=(rev*10)+b

    c=c/10

print rev

if (temp==rev):

    print "palindrome"

else:

    print "no"
