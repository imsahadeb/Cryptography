##BBS Blum Blum Shub
##It is a Random Number Generator

p=int(input("Enter the first prime number: "))
q=int(input("Enter the second prime number: "))

m=p*q
seed = int(input("Enter the seed Value: "))
r=int(input("Enter the range of the Random Number: "))
for i in range(0,r):
    seed =(seed*seed)%mls
    b=seed%2
    if(b==0):
        print("0",end="")
    else:
        print("1",end="")

print("")
       