# Q Loop through a list of numbers, skip negatives, 
# stop if you hit zero, print the rest

numbers = [4, -3, 8, -1, 15, 0, 23, -7, 42]

for i in numbers:
    if i < 0:
        continue
    elif i == 0:
        break
    else:
        print(i)
