'''
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        freq = {}
        count = 0
        res = []
        for num in nums:
            cum_sum += num
            if cum_sum == k :
                count += 1
            if cum_sum - k in freq:
                count += freq[cum_sum - k] 
            if cum_sum in freq:
                freq[cum_sum] += 1
            else:
                freq[cum_sum] = 1
        return count