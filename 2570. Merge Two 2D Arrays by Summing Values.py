class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        id1, id2 = 0, 0
        size1, size2 = len(nums1), len(nums2)
        res = []
        while id1 < size1 and id2 < size2:
            if nums1[id1][0] == nums2[id2][0]:
                res.append([nums1[id1][0], nums1[id1][1] + nums2[id2][1]])
                id1 += 1
                id2 += 1
            elif nums1[id1][0] < nums2[id2][0]:
                res.append([nums1[id1][0], nums1[id1][1]])
                id1 += 1
            else:
                res.append([nums2[id2][0], nums2[id2][1]])
                id2 += 1
            
        while id1 < size1:
            res.append([nums1[id1][0], nums1[id1][1]])
            id1 += 1
        
        while id2 < size2:
            res.append([nums2[id2][0], nums2[id2][1]])
            id2 += 1

        return res