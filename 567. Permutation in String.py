class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # TLE solution
        # dic1 = {}
        # for i in range(len(s1)):
        #     dic1[s1[i]] = 1 + dic1.get(s1[i], 0)

        # l = 0
        # k = len(s1)

        # for r in range(len(s2)):
        #     dic2 = {}
        #     while (r - l + 1) > k:
        #         l += 1
            
        #     for i in range(l, r + 1):
        #         dic2[s2[i]] = 1 + dic2.get(s2[i], 0)
            
        #     if dic1 == dic2:
        #         return True
        
        # return False

        dic1 = {}
        for char in s1:
            dic1[char] = dic1.get(char, 0) + 1

        l = 0
        k = len(s1)
        dic2 = {}

        for r in range(len(s2)):
            char_r = s2[r]
            if char_r in dic1:
                dic2[char_r] = dic2.get(char_r, 0) + 1

            if r - l + 1 == k:
                if dic1 == dic2:
                    return True

                char_l = s2[l]
                if char_l in dic1:
                    dic2[char_l] -= 1
                    if dic2[char_l] == 0:
                        del dic2[char_l]
                l += 1
                
        return False