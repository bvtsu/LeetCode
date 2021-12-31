class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 #counter for consecutive ones in a given list
        MaxOnes = 0 #used to store max counter value
        for vals in nums: #loop through list
            if vals == 0:
                counter = 0 #if zero, reset counter
            else:
                counter+=1 #otherwise, keep adding to counter
                MaxOnes=max(MaxOnes,counter) #only retain max counter value
        return(MaxOnes)