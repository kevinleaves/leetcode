class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combo = []
        leftN = rightN = 0

        def recurse(leftN, rightN):
            # base case
            if n == leftN == rightN:
                res.append("".join(combo))
                return
            # add opens
            if leftN < n:
                combo.append("(")
                recurse(leftN + 1, rightN)
                combo.pop()
            # add closes
            if rightN < leftN:
                combo.append(")")
                recurse(leftN, rightN + 1)
                combo.pop()

        recurse(leftN, rightN)
        return res
