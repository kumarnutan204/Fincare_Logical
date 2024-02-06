print("Hello")
num= (int)(input("Enter number to check if its prime"))

def prime(num):
    flag=1
    if(num==0 or num==1):
        print("Not a prime")
    
    for i in range(2,(int)(num/2)+1):
        if((num%i)==0):
            flag=0
    if(flag==1):
        print(" prime")
    else:
        print("not a prime")

prime(num)
    
