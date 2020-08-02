from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        标准广度优先搜索，对于一个拓展出去的状态树来说
        一旦找到endword，那么就一定是最短路径
        更新变量设置：current_word 和 level
            level永远是current_word的“层次”
            每次下降下去，current_word不断更新，下一列的层次level+1
        """
        # 首先要对wordlist进行一个预处理，取出所有的邻接表
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # 既然所有单词都具有相同的长度
        L = len(beginWord)

        # key是通用状态，value是[]，承装所有对应通用状态的单词
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+'*'+ word[i+1:]].append(word)
                print(all_combo_dict)

        # 广度优先搜索队列
        queue = [(beginWord,1)]
        visited = {beginWord:True}
        while queue:
            current_word,level = queue.pop(0)
            # 找出当前所有current_word的通用状态
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                # 检查这些通用状态是否对应其他单词
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord: # 说明在邻接表中找到了
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,level+1))
        return 0

solu = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solu.ladderLength(beginWord,endWord,wordList))


