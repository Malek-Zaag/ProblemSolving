#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
import threading
class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()
        # create another lock to control sequence between second and third functions
        self.lock2 = threading.Lock()
        self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock1.acquire()
        printSecond()
        self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.lock2.acquire()
        printThird()
        

# @lc code=end

