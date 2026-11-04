def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))
    return result
    
# Write a function that finds the maximum element in each sliding window of size k in an array. Return a list of maximums for each window position.

# The function should:
# - Slide a window of size k through the array
# - Find the maximum element in each window position
# - Return a list of maximum values
# - Handle edge cases (empty array, k <= 0, k > array length)
# - Return empty list for invalid inputs
