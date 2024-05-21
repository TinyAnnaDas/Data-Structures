# 2. Write a program to print all unique elements in an array.
my_array = [13, 53, 53, 52, 21, 1, 2]


element_count = {}
for element in my_array:
   element_count[element] = element_count.get(element, 0) + 1


unique_elements_array = []
for key in element_count.keys():
   if element_count[key] ==1:
      unique_elements_array.append(key)


print ("The unique elements in the array are : ", unique_elements_array)