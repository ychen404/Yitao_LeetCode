class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        print(m, n, l)
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        
        C = [[0 for _ in range(l)] for _ in range(m)]
        # print(C)
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB:
                            C[i][j] += eleA * eleB
                            # print(f"eleB = {eleB}")
                            # print(f"i = {i}, j = {j}")
        return C
