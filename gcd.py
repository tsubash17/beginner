def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:""\n"))
b=int(input("Enter second number:""\n"))
print(gcd(a,b))
