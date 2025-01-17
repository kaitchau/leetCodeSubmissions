class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        highest_altitude = 0
        for net in gain:
            altitude= altitude+net
            if altitude > highest_altitude:
                highest_altitude = altitude
        return highest_altitude
        