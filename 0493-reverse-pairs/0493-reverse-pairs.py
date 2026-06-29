class Solution:
    def mergelist(self,arr1: list[int],arr2: list[int]) -> tuple(list[int],int):
        n = len(arr1)
        m = len(arr2)
        count = 0
        result = []
        j=0

        for i  in range(0,n):
            while j<m and arr1[i]>2*arr2[j]:
                j+=1
            count += j

        i=0
        j=0
        while i<n and j<m:
            if arr1[i]<=arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j+=1
        
        while i<n:
            result.append(arr1[i])
            i+=1
        while j<m:
            result.append(arr2[j])
            j+=1
        return result,count
    
    def mergesort(self,lst: list[int]) -> tuple(list[int],int):
        if len(lst)<=1:
            return lst,0
        mid = len(lst)//2
        first_half = lst[:mid]
        second_half =lst[mid:]

        fh,cnt1 =self.mergesort(first_half)
        sh,cnt2 = self.mergesort(second_half)

        merged,count=self.mergelist(fh,sh)
        return merged,cnt1+cnt2+count

    def reversePairs(self, nums: List[int]) -> int:
        m,count = self.mergesort(nums)
        return count
        