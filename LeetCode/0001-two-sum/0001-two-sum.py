class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for x, i in zip(range(n), range(n - 1, -1, -1)):          # x: 0..n-1, i: n-1..0
            for y, j in zip(range(n), range(n - 1, -1, -1)):      # y: 0..n-1, j: n-1..0
                # forward pair (x, y)
                if x != y and nums[x] + nums[y] == target:
                    return [x, y]

                # backward pair (i, j)
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


        return []
