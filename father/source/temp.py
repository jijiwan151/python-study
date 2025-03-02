a = [1, 3, 4, 2, 45, 3, 5, 3, 5, 3,6, 6, 3, 6, 3, 65, 436, 3, 5,3 4,6,5 34, 65, 43, 564, 43, 65, 43, 54,43, 6,4 5,3 265,43]

removed_number_list = []

for i in a:
    if (i != 3):
        removed_number_list.append(i)

del a
print(removed_number_list)

print('test')