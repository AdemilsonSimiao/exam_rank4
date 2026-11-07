def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n < 2:
        return 0
    pal = [[False] * n for _ in range(n)]
    cuts = [0] * n
    for end in range(n):
        best = end
        for start in range(end + 1):
            is_palindrome = (
                s[start] == s[end]
                and (end - start <= 1 or pal[start + 1][end - 1])
            )
            if is_palindrome:
                pal[start][end] = True
                if start == 0:
                    best = 0
                else:
                    best = min(best, cuts[start - 1] + 1)
        cuts[end] = best
    return cuts[-1]

# Given a string `s`, find the minimum number of cuts needed to partition it such that every resulting substring is a palindrome.

# A cut divides the string between two characters. With `c` cuts, the string is split into `c + 1` substrings. We want the minimum number of cuts `c` such that all parts are palindromes.

# Return this minimum number of cuts (an integer).

# Constraints:
# - An empty string or a string of length 1 is already a palindrome -> 0 cuts.
# - If the entire string is already a palindrome -> 0 cuts.
# - In the worst case (all characters are distinct), the result is len(s) - 1 cuts.