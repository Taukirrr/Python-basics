# Write a function that returns the largest number from a list (no using max())

def maximum(list1):
    max_element  =  list1[0]
    
    for i in list1 :
        if i >max_element:
            max_element = i
    
    return max_element
list1 = [10,20,40,70,100,89,23,43,64]
print("max element:",maximum(list1))
