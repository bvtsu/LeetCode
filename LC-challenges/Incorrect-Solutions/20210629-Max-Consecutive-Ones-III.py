from typing import List
class Solution():
    def longestOnes(self, nums: List[int], k: int) -> int:
        #print(nums,k)
        counter = 0
        MaxOnes = 0
        OneCounts=[]
        i = 0
        while i < len(nums):
            if nums[i]==1:
                MaxOnes+=1
            else:
                counter+=1
                if counter<=k:
                    MaxOnes+=1
                elif counter>k:
                    counter=0
                    OneCounts.append(MaxOnes)
                    MaxOnes=0
                    i=sum(OneCounts)-k-1
            i+=1
        print(OneCounts)
        return(max(OneCounts))
            


test_list=Solution()
test_list.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)