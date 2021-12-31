'''
17 / 48 test cases passed.
Status: Time Limit Exceeded
'''

from typing import List
import numpy as np #Numpy allows use of lists to index arrays

class Solution(object):
    def longestOnes(self, nums: List[int], k: int) -> int:
        np_nums=np.array(nums,dtype=int) #Convert list to np.array
        counter = 0 #counter for consecutive ones after flipping k 0's
        MaxOnes = 0 #used to store max counter value per loop
        zero_indices = [i for i, x in enumerate(np_nums) if x == 0] #indices of original 0's
        if sum(np_nums==0) < k: #shortcut if there are less zeros than k flips allowed
            return(len(np_nums))
        for y in range(0,len(zero_indices)-k+1): #incrementally loop through zero_indices
            np_nums[zero_indices[y:y+k]]=np.array([1]*(k),dtype=int) #flip k 0's to 1's
            for vals in np_nums: #loop through list with newly flipped values
                if vals == 0:
                    counter = 0 #if zero, reset counter
                else:
                    counter+=1 #otherwise, keep adding to counter
                    MaxOnes=max(MaxOnes,counter) #only retain max counter value per flip
            #OneCounts.append(MaxOnes) #append max counter value from the flip
            np_nums[zero_indices[y:y+k]]=np.array([0]*(k),dtype=int) #undo flip
            #MaxOnes=0 #reset max counter value
            counter=0 #reset counter for consecutive ones
        return(MaxOnes)