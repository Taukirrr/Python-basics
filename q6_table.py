# Print a multiplication table for any number the user enters

num = int(input("enter input:"))
print("table of",num)
for i in range(1,11):
    ans = num*i
    print(num ,"*" , i ,"=" ,ans)
