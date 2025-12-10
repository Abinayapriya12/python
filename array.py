def merge_arr(arr1,arr2):
    return sorted(set(arr1+arr2))
a=[1,3]
b=[2,4]
c=merge_arr(a,b)
print(c)
