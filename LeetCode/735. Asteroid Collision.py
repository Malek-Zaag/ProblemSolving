class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        j=0
        for i in asteroids:
            while j >0 and asteroids[j - 1] > 0 and i < 0 and asteroids[j - 1] < abs(i):
                j-=1
            if j == 0 or i > 0 or asteroids[j - 1] < 0:
                asteroids[j] = i
                j += 1
            elif asteroids[j - 1] == abs(i):
                j -= 1
        return asteroids[:j]
