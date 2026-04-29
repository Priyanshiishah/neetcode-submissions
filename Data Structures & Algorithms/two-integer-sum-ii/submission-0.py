class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l<r:
            carSum = numbers[l] + numbers[r]
            if carSum > target:
                r -= 1
            elif carSum < target:
                l += 1
            else:
                return [l+1,r+1]
        return []