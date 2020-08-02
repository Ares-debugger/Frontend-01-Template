import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        dic = collections.defaultdict(list)

        # 邻接表预处理
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)

        # 广度优先遍历，每次遍历都记录当前层次的节点和路径
        # 实际上用两个队列进行处理，也是一种常见的思想
        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen = set()
        res = []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: return res
            q, s = s, q
        return []

solu = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solu.findLadders(beginWord,endWord,wordList))


