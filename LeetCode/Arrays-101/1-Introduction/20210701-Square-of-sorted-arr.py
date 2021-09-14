class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #map(lamba function applied to x: square x,list) maps lamdba function onto all elements in a list
        return(sorted(map(lambda x: x ** 2, nums)))