from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    q.append(j)
                    if j == len(s) - 1:
                       return True
            farthest = i + maxJump

        return False

# Example usage
sol = Solution()
print(sol.canReach("011010", 2, 3))  # Output: True
print(sol.canReach("000100000000", 2, 3))  # Output: True
