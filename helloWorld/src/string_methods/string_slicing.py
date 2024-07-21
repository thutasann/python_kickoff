print("--------------- STRING SLICING (INDEXING) ---------------- ")

# slicing => create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]
# start: The starting index of the slice (inclusive).
# end: The ending index of the slice (exclusive).
# step: The step size, which determines how many characters to skip between each character in the slice.

name = "Bro Code"

first_name = name[0:3]
last_name = name[4:]
funky_name = name[0:8:1]
reversed_name = name[::-1]

print("string_length " + str(len(name)))
print("first_name " + first_name)
print("last_name " + last_name)
print("funky_name " + funky_name)
print("reversed_name " + reversed_name)

text = "Hello, World"
sliced_text = text[0:12:2]
# "Hlo ol" (every second character from index 0 to 11)
print("sliced_hello_world " + sliced_text)

print("--------------- STRING SLICING (SLICE METHOD) ---------------- ")

website1 = "https://google.com"
website2 = "https://wikipedia.com/"
slice = slice(7, -4)

print("sliced_website 1 " + website1[slice])
print("sliced_website 2 " + website2[slice])
