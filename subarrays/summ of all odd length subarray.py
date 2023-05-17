class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0   
        i = 0
        while i < len(arr):
            total += arr[i] #here we are adding [1],[2],[3],[4]
            j = i + 1
            while j < len(arr):
                if (j-i+1) % 2 != 0:
                    total =total+sum(arr[i:j+1])  
                j += 1
            i += 1 
        return total
        
"""
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[1,4,2] = 7
[1,4,2,5,3] = 15
[4] = 4
[4,2,5] = 11
[2] = 2
[2,5,3] = 10
[5] = 5
[3] = 3
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""