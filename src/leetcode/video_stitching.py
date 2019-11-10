class Solution:
    def videoStitching(self, clips, t):
        if t == 0:
            return 0

        clips.sort()

        if clips[0][0] != 0:
            return -1

        counter = 1
        current_index = 0

        while current_index + 1 < len(clips) and clips[current_index+1][0] == 0:
            current_index += 1

        right = clips[current_index][1]

        while right < t and current_index < len(clips):
            new_index = current_index + 1
            max_right = -1
            max_index = -1
            while new_index < len(clips) and clips[new_index][0] <= right:
                if clips[new_index][1] > max_right:
                    max_right = clips[new_index][1]
                    max_index = new_index
                new_index += 1
            if max_right <= right:
                return -1
            right = max_right
            current_index = max_index
            counter += 1
            if right >= t:
                return counter

        return -1 if right < t else counter


solution = Solution()

# clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
# t = 10
# assert solution.videoStitching(clips, t) == 3
#
# clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
#          [5, 7], [6, 9]]
# t = 9
# assert solution.videoStitching(clips, t) == 3
#
# clips = [[0, 1], [1, 2]]
# t = 5
# assert solution.videoStitching(clips, t) == -1
#
# clips = [[0, 4], [2, 8]]
# t = 5
# assert solution.videoStitching(clips, t) == 2

clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
         [5, 7], [6, 9]]
t = 9
assert solution.videoStitching(clips, t) == 3
