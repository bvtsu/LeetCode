class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = [i for i in arr] #duplicate list
        arr_trace = 0 #use to keep arr in line with arr2 after inserting zeroes
        for x in range(len(arr2)): #arr2 is our ref
            if arr2[x]==0: #if the ref val is zero
                arr.insert(x+arr_trace,0) #add a zero to the corresponding index in arr, other eles are +1 index
                arr.pop() #remove the last item
                arr_trace+=1 #corresponds to zeroes added to arr