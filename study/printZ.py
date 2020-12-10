from typing import List
'''def removeDuplicates(nums):
    j=1
    while j<len(nums):
        if nums[j-1] == nums[j]:
            nums.remove(nums[j])
        else:
            j+=1
    return len(nums)'''

def maxProfit(prices):
    sum1,count,i=0,0,0
    while(i<len(prices)):
        max = i
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[max]:
                max = j
            else:
                break
        count = prices[max] - prices[i]
        i = max + 1
        sum1 += count
    return sum1

if __name__ == '__main__':
    print(maxProfit([1,2,3,4,5]))