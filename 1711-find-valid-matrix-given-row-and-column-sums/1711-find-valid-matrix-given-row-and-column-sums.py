class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        Sum = sum(rowSum) + sum(colSum)

        M = [[0 for _ in range (len(colSum))] for _ in range (len(rowSum))]
        while sum(rowSum) > 0 :
            R = [i for i in rowSum if i != 0]
            C = [i for i in colSum if i != 0]
            i= rowSum.index(min(R))
            j= colSum.index(min(C))
            M[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= M[i][j]
            colSum[j] -= M[i][j]
        return M