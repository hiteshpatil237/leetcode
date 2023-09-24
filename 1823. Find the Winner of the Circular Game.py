class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def get_index(curr_index, steps, length):
            new_index = curr_index + steps - 1
            if new_index >= length:
                new_index %= length
            return new_index

        def get_answer(arr, index):
            length = len(arr)
            if length == 1:
                return arr[0]
            else:
                arr.pop(index)
                return get_answer(arr, get_index(index, k, length - 1))

        return get_answer([i for i in range(1, n + 1)], get_index(0, k, n))