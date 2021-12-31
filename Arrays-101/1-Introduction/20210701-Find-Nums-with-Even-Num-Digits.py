class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digit_counter=0
        even_counter=0
        for x in nums: #for each x in nums
            while (x > 0): #while x is > 0
                x = x//10 #re-store x as one digit less than original using floor division
                digit_counter = digit_counter + 1 #increment +1 to digit, then go back through loop til all digits are counted
            #print(digit_counter)
            if (digit_counter % 2) == 0: #check for evens, must be divisible by 2 with no remainder
                even_counter+=1 #increment +1 to even counter
            else:
                pass #do nothing because digit count is odd
            digit_counter=0 #reset digit counter for the next x in nums
        return(even_counter)