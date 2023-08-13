def interest(p1,r1,t1 ):
    i=p*r*t/100
    return(i)
p=int(input("Enter principle="))
r=int(input("Enter rate="))
t=int(input("Enter time="))
in1=interest(p,r,t)
print("Interest=",in1)
