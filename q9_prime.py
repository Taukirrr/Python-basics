#Q Write a function that checks if a number is prime 
#— return True or False


def check_prime(num):
    if(num < 2):
        return False
    if num in (2,3):
        return True
    if(num%2 == 0):
        return False
    for i in range(3,int(num**(0.5))+1,2):
        if(num%i == 0):
            return False
    return True
      
num = int(input("enter no <=0 :")) 
ans = check_prime(num)
print(ans)