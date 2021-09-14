class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupe_list=[]
        idx=0
        while idx < len(nums): #keep going through the list
            if nums[idx] in dupe_list: #if a dupe shows up
                nums.pop(idx) #destroy at the given index, moving everything forward
            else:
                dupe_list.append(nums[idx]) #add non-dupe for future checks
                idx+=1 #increment to see if next idx is a dupe