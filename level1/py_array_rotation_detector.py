def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if not arr1 and not arr2:
        return True
    if not len(arr1) == len(arr2):
        return False

# Write a Python function that takes two lists (arrays) as parameters and determines if the second list is a rotation of the first list (left or right).

# A rotation means that the elements are shifted circularly. For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

# The function must return True if arr2 is a rotation of arr1, and False otherwise.
# If the arrays have different lengths, they cannot be rotations of each other.
# Two empty arrays are considered rotations of each other.