"""
238. PRODUCT OF ARRAY EXCEPT SELF
Given an integer array nums, return an array answer such that answer[i] is equal
 to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def product_except_self(nums: list[int]) -> list[int]:
    answer: list[int] = [0] * len(nums)

    left: int = 1
    for i in range(len(nums)):
        answer[i] = left
        left *= nums[i]

    right: int = 1
    for i in range(len(nums) - 1, -1, - 1):
        answer[i] = answer[i] * right

        right *= nums[i]

    return answer

print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1,1,0,-3,3]))
