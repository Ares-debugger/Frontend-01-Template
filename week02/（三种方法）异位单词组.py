import collections

class Solution(object):
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        如果当前的str不和任何一个map里面的str是一个模式
        那么就=[]
        如果和里面的元素是同一个模式
        那么就append
        结果：超时
        """
        def isAnagram(s,t):
            countDic = {}
            for char in s:
                if char not in countDic:
                    countDic[char] = 1
                else:
                    countDic[char] += 1
            for char in t:
                if char not in countDic:
                    return False
                else:
                    countDic[char] -= 1
            for char in countDic:
                if countDic[char] != 0:
                    return False
            return True

        modeDic = {}
        res = []
        visited = set()
        for str in strs:
            if len(modeDic) == 0:
                modeDic[str] = [str]
                visited.add(str)
                continue
            for mode in list(modeDic.keys()):
                if isAnagram(mode,str):
                    modeDic[mode].append(str)
                    visited.add(str)
            # 如果str到这里没有被用到过，那么才会执行下面的语句
            if str not in visited:
                modeDic[str] = [str]
        for mode in modeDic:
            res.append(modeDic[mode])
        return res

    def groupAnagrams2(self,strs):
        ans = collections.defaultdict(list)
        for str in strs:
            ans[tuple(sorted(str))].append(str)
            '''
            sorted(str)-> ['letterA','letterB'....] 只有这样保证唯一性
            tuple()-> ('letterA','letterB'....) -> 元组做key保证合法性
            '''
        return ans.values()

    def groupAnagrams3(self, strs):
        '''
        :param strs:
        :return:
        构建一个26维度的向量，用ord表示ascall码，减去'a'的码值得到0-26
        以tuple列表作为key传入即可
        '''
        ans = collections.defaultdict(list)
        count = [0]*26
        for str in strs:
            for char in str:
                count[ord(char)-ord('a')] += 1 # 这样可以不考虑顺序了，本质上仍然是维护一个hash表
            ans[tuple(count)].append(str)
        return ans.values()

solu = Solution()
print(solu.groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"]))