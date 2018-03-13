a=input()
if a>1:
    for i in range(2,a):
        (a%i==0)
        print (a,"it's composite num")
        break
    else:
        print ("prime num",a)
