# 6. Write a program to find the largest and smallest number in an array.

new_array = [5, 2, 1, 3, 9, 10]

largest = new_array[0]
smallest = new_array[0]


for element in new_array:
    if element > largest:
        largest = element
    if element < smallest:
        smallest = element 


print("The largest value in the array is : ",largest, "and the smallest is ", smallest)
