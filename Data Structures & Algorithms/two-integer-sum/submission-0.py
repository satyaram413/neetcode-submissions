class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for i, v in enumerate(nums):
            diff= target-v
            if diff not in d:
                d[v]=i
            else:
                l.append(d[diff])
                l.append(i)
        return l

        