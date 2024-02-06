print("Hello")

def perfect(num):
    sum=0
    for i in range(1,num):
        if((num % i) == 0):
            #print(i)
            sum+=i
    if(sum==num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} number is not a perfect number")

for i in range(1,200):    
    perfect(i)
