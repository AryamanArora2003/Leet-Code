class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        n = n

        length= len(flowerbed)

        for i in range(len(flowerbed)):
            left = flowerbed[i-1] if i > 0 else flowerbed[i]
            right = flowerbed[i+1] if i<(length-1) else flowerbed[i]
            curr = flowerbed[i]

            if (curr,left,right)==(0,0,0):
                flowerbed[i]=1
                n -= 1

        if n<=0:
            return True
        else:
            return False




