class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n > 0:
            max_nums1_idx = len(nums1)-1 #set index at the back to be replaced by highest num
            m -= 1
            n -= 1
            while m >= 0 and n >= 0: #as long as there's still m and n nums to merge
                if nums1[m] >= nums2[n]: #if the current highest val by sliding index is in nums1
                    nums1[max_nums1_idx] = nums1[m] #store to the corresponding index in nums1
                    nums1[m]=0
                    m -= 1 #move index tracker down for mergeable values in nums1   
                elif nums2[n] >= nums1[m]:
                    nums1[max_nums1_idx] = nums2[n]
                    n -= 1  #move index tracker down for mergeable values in nums2
                max_nums1_idx -= 1  #move index tracker down for final nums1 indices
            if m < 0: #when m mergeables run out, the "while loop" ends, but n mergeables may still be >= 0
                for i in range(n+1): #for the remaining indices from nums2
                    nums1[i]=nums2[i] #move associated values to the corresponding spots in nums1
        else:
            if m == 0: #when no mergeables from nums1, just move all n mergeables from nums2 to nums1
                for i in range(n):
                    nums1[i]=nums2[i]
            if n == 0:
                pass #if no n mergeables from nums2, don't need to do anything