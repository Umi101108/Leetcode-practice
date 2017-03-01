"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = len(nums1), len(nums2)
        if a > b:
            nums1, nums2, a, b = nums2, nums1, b, a
        if b == 0:
            raise ValueError

        imin, imax, half_len = 0, b, (a + b + 1)/2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < a and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (a + b) % 2 == 1:
                    return max_of_left
                if i == a: min_of_right = nums2[j]
                elif j == b: min_of_right = nums1[i]

                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

l1 = [1, 4, 5, 6]
l2 = [3, 2]
so = Solution()
print so.findMedianSortedArrays(l1, l2)
