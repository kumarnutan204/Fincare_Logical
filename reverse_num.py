num=(int)(input("Enter number to reverse"))

def reverse(num):
    reversed=0
    while(num!=0):
        remainder=num%10
        reversed=(reversed*10)+remainder
        num=num//10
    
    print(reversed)

reverse(num)
