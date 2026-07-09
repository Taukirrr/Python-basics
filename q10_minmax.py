#Q Ask user to enter 5 numbers one by one, store in a list, 
# print min and max without using built-in functions

mylist =[]
for i in range(1,6):
    n = int(input("enter no. : "))
    mylist.append(n)
max = mylist[0]
min = mylist[0]


for i in mylist:
    if(max<i):
        max = i
    if(min>i):
        min = i
    
print(mylist)
print("maximum ",max)
print("minimum ",min)