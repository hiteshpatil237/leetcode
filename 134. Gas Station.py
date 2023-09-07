class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        current_gas = 0
        start_station = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_station = i + 1
                current_gas = 0
            
        if total_gas >= 0:
            return start_station
        else:
            return -1