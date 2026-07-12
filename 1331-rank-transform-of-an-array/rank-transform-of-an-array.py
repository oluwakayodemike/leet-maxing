class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cleaned = sorted(set(arr)) 
        val_dict = {}
        result = []

        for i in range(len(cleaned)):
            val_dict[cleaned[i]] = i + 1
        
        for i in range(len(arr)):
            result.append(val_dict[arr[i]])

        return result