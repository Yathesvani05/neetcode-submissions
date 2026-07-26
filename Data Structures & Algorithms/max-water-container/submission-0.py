class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        l=0
        r=len(heights)-1
        while l<r:
            w=r-l
            area=w*min(heights[l],heights[r])
            maxi=max(area,maxi)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxi
        