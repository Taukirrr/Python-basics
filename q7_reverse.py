#Write a function that takes a string and returns it reversed (no slicing shortcuts)

def reverse(original_string):
    reverse_string = ""
    for char in original_string:
        reverse_string = char + reverse_string
    return reverse_string

original_string = "Taukir"
newreversed_string = reverse(original_string)
print(newreversed_string)
