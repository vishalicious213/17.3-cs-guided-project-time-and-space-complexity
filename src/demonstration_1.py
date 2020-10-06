"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""
def remove_duplicates(nums):
    # Your code here

"""
Given a sorted array `nums`, remove the duplicates from the array.
Example 1:
Given nums = [0, 1, 2, 3, 3, 3, 4]
Your function should return [0, 1, 2, 3, 4]
Example 2:
Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
Your function should return [0, 1, 2, 3, 4, 5].
*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""
def remove_duplicates(nums):
    # UPER
    # UNDERSTAND
    # Our goal is to remove the duplicates
    # the array is already sorted
    # numbers don't necessarily have to be consecutive
    # Will they all be ints? let's assume.
    # length indicates the end of the array after removing duplicates (for in place solution)
    # PLAN
    # turn the list into a set --> automatically remove duplicates b/c that's what sets do
    # OUT OF PLACE
    # runtime: O(n)
    # space complexity: O(n)
    nums_set = set()
    for num in nums:
        nums_set.add(num)
    return list(nums_set)
    # turn it into a dictionary to eliminate duplicate keys -- similar to the set approach
    # loop w/in a loop to check each variable against the other variables
    # could use a conditional in a list comprehension? maybe?
def remove_duplicates_in_place(nums):
    # in place means we don't use extra space -- means we have to swap / move numbers around within `nums`
    # we can run a for loop
    # Overall runtime: O(n^2)
    # Space complexity: O(1)
    i = 0  # O(1)
    while i < len(nums) - 1:  # how many times do the loop run? O(n)
        if nums[i] == nums[i+1]:        # O(1)
            nums.pop(i+1)  # remove the element at index i+1    # O(n)
        else:
            i = i + 1
        # remove it from the list
    return nums
def remove_duplicates_in_place_linear(nums):
    # runtime: O(n)
    # space complexity: O(1)
    # iterate through the list
    # keep one non_duplicate_index pointing to the end of the part of the array w/ no duplicates
    non_duplicate_index = 1
    # and another idx pointing to the "current" element in the array
    for current_index in range(1, len(nums)):
        # if current element is already in the non-duplicate part of the array,
            if nums[current_index] == nums[non_duplicate_index - 1]:
                # skip it
                continue
            else:
                # otherwise, set nums[non_duplicate_index] to current element and increment non_duplicate_index
                nums[non_duplicate_index] = nums[current_index]
                non_duplicate_index += 1
    return nums, non_duplicate_index
    # [0, 1, 2, 3, 4, 3, 4]
    #                 ^
    #                    ^
nums, l = remove_duplicates_in_place_linear([0, 1, 2, 3, 3, 3, 4])
print(nums, l)