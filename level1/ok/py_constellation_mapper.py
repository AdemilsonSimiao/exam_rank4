def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [['.' for _ in range(dim)] for _ in range(dim)]
    for r, c in stars:
        if 0 <= r < dim and 0 <= c < dim:
            grid[r][c] = '*'
    return ["".join(row) for row in grid]

# Write a function that maps a constellation of stars onto a grid and returns the visual representation as a list of strings.

# The function should:
# - Take a list of star coordinates as tuples (row, col) and grid size as integer
# - Return a list of strings representing the grid
# - Stars are represented by '*' and empty spaces by '.'
# - Grid coordinates start from (0, 0) at top-left
# - Ignore coordinates outside the grid boundaries
# - Handle duplicate coordinates (star appears only once)