# Write a program to count the total number of duplicate elements in an array.

the_array = [34, 56, 45, 23, 34, 45]


number_of_times = 0

element_counts = {}

for element in the_array:
    if element in element_counts: # in is also applicable to dictionaries for checking if similar key is present
        element_counts[element] += 1
    else:
        element_counts[element] = 1

# print(element_counts)


duplicate_counts = 0

for count in element_counts.values(): # looping through the dictionary values. 
    if count > 1:
        duplicate_counts +=1

print("Total number of duplicate elements : ", duplicate_counts)



