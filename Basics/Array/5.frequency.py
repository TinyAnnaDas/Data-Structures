
# 5. Write a program to count the frequency of each element of an array.

my_array = [1,3,4,2,1,9,3,5,4]


frequency_dict = {}

for element in my_array:
    if element in frequency_dict:
        frequency_dict[element] += 1
    else:
        frequency_dict[element] = 1

print("The frequency of each element is :")

for key, value in frequency_dict.items():
    print(key, "occurs", value, "times")


