class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        li=[]
        while l<r:
            if(numbers[l]+numbers[r]==target):
                li.append(l+1)
                li.append(r+1)
                return li
            elif(numbers[l]+numbers[r]>target):
                r-=1
            else:
                l+=1
        