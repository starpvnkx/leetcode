"""
49. GROUP ANAGRAMS
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each 
other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to 
form each other.


Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:

    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars: dict[str, int] = {}

        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        for c in t:
            if c not in chars:
                return False
            chars[c] -= 1
            if chars[c] <= 0:
                del chars[c]

        return True

    visited: list[str] = []
    groups: list[str] = []

    for i in range(len(strs)):
        s: str = strs[i]
        if s in visited:
            continue
        visited.append(s)
        anagrams: list[str] = [s]
        for j in range(i+1, len(strs)):
            t: str = strs[j]
            if is_anagram(s, t):
                anagrams.append(t)
                visited.append(t)

        groups.append(anagrams)
        
    return groups

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))