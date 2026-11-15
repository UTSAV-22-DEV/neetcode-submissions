class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax=0,0
        l,r=0,len(height)-1
        watertrapped=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>lmax:
                    lmax=height[l]
                else:
                    watertrapped+=lmax-height[l]
                l+=1
            else:
                if height[r]>rmax:
                    rmax=height[r]
                else:
                    watertrapped+=rmax-height[r]
                r-=1
        return watertrapped