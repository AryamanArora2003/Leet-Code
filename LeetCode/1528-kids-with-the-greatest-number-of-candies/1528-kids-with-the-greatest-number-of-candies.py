class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = [False]*len(candies)
        largest = 0 
        for i in range(len(candies)):

            temp = candies[i]
            if temp>largest:
                largest = temp

        for i in range(len(candies )):
            checkGreatest = candies[i] + extraCandies

            if checkGreatest>=largest:
                result[i] = True

        return result

            

        
