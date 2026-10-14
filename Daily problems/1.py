array=[]
nums=[3,2,4]
target=6
for i in range (len(nums)):
    for j in range(len(nums)):
        if j==i:
            continue
        if (nums[i]+nums[j])==target:
            array.append(i)
            array.append(j)
            print(array)