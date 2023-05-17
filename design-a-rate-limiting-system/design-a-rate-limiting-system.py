class RateLimiter:

    def __init__(self, n: int, t: int):
        self.n = n
        self.t = t
        self.allowed = collections.deque()

    def shouldAllow(self, timestamp: int) -> bool:
        if not self.allowed:
            self.allowed.appendleft(timestamp)
            return True
        
        while self.allowed and timestamp - self.allowed[-1] >= self.t:
            self.allowed.pop()
        
        if len(self.allowed) >= self.n:
            return False
        
        self.allowed.appendleft(timestamp)
        return True
            
        
            
            


# Your RateLimiter object will be instantiated and called as such:
# obj = RateLimiter(n, t)
# param_1 = obj.shouldAllow(timestamp)