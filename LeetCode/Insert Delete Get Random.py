import random
class RandomizedSet:

    def __init__(self):
        self.seed=random.seed(10)
        self.s=set()

    def insert(self, val: int) -> bool:
        if val in list(self.s):
            return False 
        else : 
            self.s.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in list(self.s):
            self.s.remove(val)
            return True 
        else : return False

    def getRandom(self) -> int:
        rg=list(self.s)
        return random.choice(rg)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()