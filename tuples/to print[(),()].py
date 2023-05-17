nums=l=[-1,0,1,2,-1,-4]
if len(nums)<3:
    print([])
out=[]
for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if(nums[i] + nums[j] + nums[k]==0):
                out.append(tuple(sorted([nums[i],nums[j],nums[k]])))
print(list(set(out)))

"""
output:
[(-1, -1, 2), (-1, 0, 1)]
"""