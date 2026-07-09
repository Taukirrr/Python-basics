sum = 0

while True:
    i = input("enter no.")
    if i == "done":
        break
    else:
        num = int(i)
        sum += num
print("total :",sum)