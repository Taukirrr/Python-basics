# Print numbers 1-50, skip multiples of 3, stop completely at first multiple of 7
for i in range(1,50):
    if i%3 == 0:
        continue
    elif i%7 == 0:
        break
    else:
        print(i)