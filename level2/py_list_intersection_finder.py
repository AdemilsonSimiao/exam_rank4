def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    ...
    
    
print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 4, 5]]))

# Write a function that finds the intersection of multiple sorted lists.
# Return a new list containing elements that appear in ALL input lists, in sorted order.

# The function should:
# - Return elements that appear in ALL lists
# - Result should be sorted in ascending order
# - Remove duplicates from the result
# - Handle empty input or empty lists gracefully
# - If any list is empty, the intersection is empty