"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freqs: dict[int, int] = {}

    for i in range(len(nums)):
        num: int = nums[i]
        if num not in freqs:
            freqs[num] = 1
        else:
            freqs[num] += 1

    sorted_keys = sorted(freqs, key=freqs.get, reverse=True)

    return sorted_keys[:k]

print(top_k_frequent( [1,1,1,2,2,3], 2))
print(top_k_frequent( [1], 1))
print(top_k_frequent( [1,2,1,2,1,2,3,1,3,2], 2))