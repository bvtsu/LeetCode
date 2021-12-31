class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Strategy 1 - simpler
        idx=0 
        while idx < len(nums): #keep going through the list
            if nums[idx]==val: #if val shows up
                nums.pop(idx) #destroy at index and move elements forward
            else:
                idx+=1 #increment to see if next idx is val
        
        #Strategy 2
        #val_indices = [i for i, x in enumerate(nums) if x == val] #indices of original vals
        #pop_slider=0 #counts number of prev deleted/popped elements
        #for i in val_indices: #for each val element
        #    nums.pop(i-pop_slider) #destroy at the given index
        #    pop_slider+=1 #+1 for each deleted element to maintain val indices