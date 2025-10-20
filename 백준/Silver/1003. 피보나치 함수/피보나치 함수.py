##피보나치 수열

## 5
## 4   3
## 3 2 2 1
## 2 1 1 0 1 0 

T = int(input())
nums = []
zero_count = [1,0]
one_count = [0,1]

for i in range(T):
    key = int(input())
    nums.append(key)

for j in range(2, max(nums)+1):
    zero_count.append(zero_count[j-1]+zero_count[j-2]) 
    one_count.append(one_count[j-1]+one_count[j-2])

for k in nums:        
    print(zero_count[k], one_count[k])
