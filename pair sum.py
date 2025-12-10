def two_sum(num,target):
    seen=set()
    for n in num:
        diff=target-n
        if diff in seen:
            return(diff,n)
        seen.add(n)
print(two_sum([2,4,6,8],10))
