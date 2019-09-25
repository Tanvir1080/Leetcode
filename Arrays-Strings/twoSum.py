class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchingNumbers = {}
        indices = []
        for index, val in enumerate(nums): 
            
            key = target - val 
            
            if key in matchingNumbers:
                indices.append(matchingNumbers[key])
                indices.append(index)
            else: 
                matchingNumbers[val] = index
                
        
        return indices