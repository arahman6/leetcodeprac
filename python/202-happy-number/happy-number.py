class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def next_num(n):
            res = 0
            while n:
                x = n % 10
                res += x ** 2
                n = n // 10
            return res
        
        while n not in visit:
            visit.add(n)
            n = next_num(n)
            if n == 1:
                return True
        
        return False



        