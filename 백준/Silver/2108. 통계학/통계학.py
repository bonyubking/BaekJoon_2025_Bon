# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
import sys


N = int(sys.stdin.readline())

nums = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    nums.append(temp)

def calculate_average(arr):
    
    sum = 0
    len = 0
    
    for temp in arr:
        sum+=temp
        len+=1
    
    if sum % len >= (len/2):
        return sum//len+1
    else: 
        return sum//len

def center_average(arr):
    arr.sort()
    return arr[(N-1)//2]

def most_count(arr):
    
    count_list = {}
    if len(arr) == 1:
        return arr[0]
    
    for num in arr:
        if num in count_list:
            count_list[num]+=1
        else:
            count_list[num]=1
    
    sorted_scores = sorted(count_list.items(), key=lambda x:(-x[1], x[0]))
    
    if sorted_scores[0][1] == sorted_scores[1][1]:
        return sorted_scores[1][0]
    else:
        return sorted_scores[0][0] 
    
    
def range(arr):
    max=-4001
    min=4001
    
    for key in arr:
        if key>=max:
            max=key
        if key<=min:
            min=key

    return max-min
       
    
    

ans1 = calculate_average(nums)
print(ans1)

ans2 = center_average(nums)
print(ans2)

ans3 = most_count(nums)
print(ans3)

ans4 = range(nums)
print(ans4)