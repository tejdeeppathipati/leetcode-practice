class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                while stack and (asteroid < 0 < stack[-1]):
                    top = stack[-1]
                    if abs(top) < abs(asteroid):
                        stack.pop()
                    elif abs(top) == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
        return stack