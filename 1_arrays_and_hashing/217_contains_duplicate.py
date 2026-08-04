"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


## First attempt
def contains_duplicate(nums: list[int]) -> bool:
    visited: dict[int, bool] = {} # alternatively use `set()`

    for num in nums:
        if num in visited:
            return True
        visited[num] = True

    return False


TESTCASES = [
    {"input": [1, 2, 3, 1], "expected": True},
    {"input": [1, 2, 3, 4], "expected": False},
    {"input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True},
]

print("Testing begins...")

for tc in TESTCASES:
    output = contains_duplicate(tc["input"])
    assert (
        output == tc["expected"]
    ), f"Testcase {tc['input']} failed. Expected {tc['expected']}, but got {output}"

print("End of testing.")

"""
Another way to solve using `set()`
def contains_duplicate(nums):
    return len(set(nums)) < len(nums)
"""
