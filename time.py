t = int(input("Enter time in minutes"))
m = t  % 60
hrs = (t - m) / 60
print (int(hrs),int(m))
