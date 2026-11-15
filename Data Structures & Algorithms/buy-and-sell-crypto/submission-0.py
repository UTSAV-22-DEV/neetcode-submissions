class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        for i in prices:
            if i<minprice:
                minprice=i
            else:
                maxprofit=max(maxprofit,i-minprice)
        return maxprofit