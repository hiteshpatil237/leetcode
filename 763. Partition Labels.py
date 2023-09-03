class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        #Maintaining a hashmap for last occrrences of character
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        #Two pointers for storing size of current partition and updating end pointer at each step
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            #Checking whether the current characters last occurence falls inside the assumed partition end
            end = max(end, lastIndex[c])

            #If condition reached where assumed partition end is equal to current character, then close partition
            if i == end:
                res.append(size)
                size = 0

        return res        