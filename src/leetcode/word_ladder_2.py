class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if len(beginWord) != len(endWord):
            return []

        dictionary = set()
        for word in wordList:
            dictionary.add(word)
        results = []
        self.recursive(beginWord, endWord, dictionary, [beginWord], results)
        return results

    def recursive(self, beginWord, endWord, dictionary, stage, results):
        if beginWord == endWord:
            results.append(stage[:])
            return

        for i in range(len(beginWord)):
            if beginWord[i] != endWord[i]:
                auxWord = beginWord[0:i] + endWord[i] + beginWord[i + 1:]
                if auxWord in dictionary:
                    stage.append(auxWord)
                    self.recursive(auxWord, endWord, dictionary, stage, results)
                    stage.pop()


sol = Solution()

print(sol.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
