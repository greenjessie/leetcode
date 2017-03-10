class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(machines) % len(machines):
            return -1
        avg = sum(machines) / len(machines)
        ans = total = 0
        for m in machines:
            total += m - avg
            ans = max(ans, abs(total), m - avg)
        return ans

s=Solution()
print(s.findMinMoves([1,2,3,4,5,6,7]))

