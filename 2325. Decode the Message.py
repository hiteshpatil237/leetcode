class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {}
        
        current = 0
        for a in key.replace(" ",""):
            if a not in mapping:
                mapping[a]=chr(current+ord('a'))
                current += 1
        ans = []
        for c in message:
            if c == " ":
                ans.append(" ")
                continue
            ans.append(mapping[c])
        return"".join(ans)
        
        # key = "the quick brown fox jumps over the lazy dog"
        # dic = {}
        # for i in key:
        #     dic[i] = dic.get(i, 0)
        # dic.pop(' ', None)
        # l = list(dic.keys())
        # new_message = list("vkbs bs t suepuv")
        # for i in range(len(new_message)):
        #     if not new_message[i] == ' ':
        #         ind = l.index(new_message[i])
        #         new_message[i] = chr(ord('a')+ind)
        # message = ''.join(new_message)