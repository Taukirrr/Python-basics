# Q Write a function that returns how many even numbers are in a list

count =0
def even_count(numbers,count):
    for i in numbers:
        if i%2 == 0:
            count = count + 1
        else:
            continue
    return count
my_list = [2,3,5,4,6,0,37,42]

print("count:",even_count(my_list,count))