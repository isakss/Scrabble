list_test = [1, 2, 3]
temp_list = list_test[:]
for i, test in enumerate(list_test):
    temp_list.pop(i)

print(temp_list)
print(list_test)