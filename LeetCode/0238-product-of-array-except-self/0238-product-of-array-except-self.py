from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        retNums = [1] * n   # hold left products first

        # left products
        product = 1
        for i in range(n):
            retNums[i] = product
            product *= nums[i]

        # right products (reuse your 'curr' index)
        curr = n - 1
        product = 1
        while curr >= 0:
            retNums[curr] *= product
            product *= nums[curr]
            curr -= 1

        return retNums



        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         product *= nums[j]
        #     retNums.append(product)

        # return retNums
