# https://leetcode.com/problems/substring-with-concatenation-of-all-words/


class PartialState:
    def __init__(self):
        self.inserts = 0
        self.words_set = {}


class Solution:
    def findSubstring(self, s, words):
        if s == '' or words == []:
            return []
        final_result = []
        words_len = len(words[0])
        words_dict = {}
        states = [[] for _ in (range(len(s) + words_len))]

        for index, word in enumerate(words):
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1

        for index in range(len(s)):
            current_word = s[index: index + words_len]

            if current_word in words_dict:
                for state in states[index]:
                    if current_word not in state.words_set:
                        state.words_set[current_word] = 1
                        state.inserts += 1
                        if state.inserts == len(words):
                            final_result.append(index - words_len * (len(words) - 1))
                        else:
                            states[index + words_len].append(state)
                    elif current_word in state.words_set:
                        if state.words_set[current_word] < words_dict[current_word]:
                            state.words_set[current_word] += 1
                            state.inserts += 1
                            if state.inserts == len(words):
                                final_result.append(index - words_len * (len(words) - 1))
                            else:
                                states[index + words_len].append(state)
                if (len(s) - index) / words_len >= len(words):
                    new_state = PartialState()
                    new_state.words_set[current_word] = 1
                    new_state.inserts = 1
                    if new_state.inserts == len(words):
                        final_result.append(index - words_len * (len(words) - 1))
                    else:
                        states[index + words_len].append(new_state)

        return final_result


s = "a"
words = ["a"]

print(Solution().findSubstring(s, words))
