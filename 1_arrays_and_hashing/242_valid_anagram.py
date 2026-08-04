"""242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters."""

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

TESTCASES = [
    {"input": ["anagram", "nagaram"], "expected": True},
    {"input": ["rat", "car"], "expected": False},
]

for tc in TESTCASES:
    out = is_anagram(tc["input"][0], tc["input"][1])
    assert (
        out == tc["expected"]
    ), f"Assertion {tc["input"]} failed. Expected {tc['expected']} bug got {out}"
