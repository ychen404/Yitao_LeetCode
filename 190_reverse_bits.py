class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            # print("n:{0:032b}".format(n))
            ret += (n & 1) << power
            # print("ret:{0:032b}".format(ret))
            n = n >> 1
            power -= 1
        return ret