class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.seen[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for j, n in vec.seen.items():
            # print(f"j={j}, n={n}")
            if j in self.seen:
                res += n * self.seen[j]
                # print(self.seen[j])
        return res
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
