"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
def contains_duplicate(nums):
    # Your code here

    # Plan1:
    # made a set
    # if set length wasn't equal to the original array length: that means there were dupes
    # Runtime: O(n)
    # space: O(n)
    pass
# Plan2:
def contains_duplicate_2(nums):
    # overall runtime: O(nlogn + n) --> O(n log n)
    # space complexity: O(1)
    nums.sort()    # sorting is usually O(n log n)
                   # nums.sort() sorts it in place
    # everything below this line is O(n)
    i = 0          # O(1)
    while i < len(nums) - 1:      # up to O(n)
        if nums[i] == nums[i+1]:  # O(1)
            return True
        i += 1
    return False
print(contains_duplicate_2([1]))