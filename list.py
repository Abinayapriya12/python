list=[1,2,2,3,3]
unique_list=[]
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
