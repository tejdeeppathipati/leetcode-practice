class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = []
        l, r = 0, 0
        n, m  = len(nums1), len(nums2)
        while l < n and r < m:
            if nums1[l] < nums2[r]:
                newArr.append(nums1[l])
                l += 1
            else:
                newArr.append(nums2[r])
                r += 1
            
        newArr.extend(nums1[l:])
        newArr.extend(nums2[r:])

        if len(newArr) % 2 == 0:
            mid1 = newArr[len(newArr) // 2 - 1]
            mid2 = newArr[(len(newArr) // 2)]
            median = (mid1 + mid2) / 2
        else:
            median = float(newArr[len(newArr) // 2 ]) 
        return median


