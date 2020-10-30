from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        usage = {}
        for key, time in zip(keyName, keyTime):
            if key not in usage:
                usage[key] = []
            usage[key].append(time)

        dangerous = []
        for key in usage:
            usage[key].sort()
            times = usage[key]
            i = 2
            while i < len(times):
                if self.oneHour(times[i - 2], times[i]):
                    dangerous.append(key)
                    break
                i += 1

        return dangerous

    def oneHour(self, firstTime: str, thirdTime: str) -> bool:
        hour1, minutes1 = self.splitTime(firstTime)
        hour2, minutes2 = self.splitTime(thirdTime)
        if hour1 == hour2:
            return True
        if hour1 == hour2 - 1 and minutes1 >= minutes2:
            return True
        return False

    def splitTime(self, time: str) -> (int, int):
        return int(time[0] + time[1]), int(time[3] + time[4])


sol = Solution()
assert sol.alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                      keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]) == ['daniel']
assert sol.alertNames(keyName=["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
                      keyTime=["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]) == ['bob']
assert sol.alertNames(keyName=["john", "john", "john"], keyTime=["23:58", "23:59", "00:01"]) == []
