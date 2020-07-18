class Solution(object):
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        暴力求解
        """
        s = sorted(s)
        t = sorted(t)
        if s==t:
            return True
        else:
            return False

    def isAngram2(self,s,t):
        '''
        :param s:
        :param t:
        :return:
        哈希表求解
        '''
        countDic = {}
        # 加上合法性判断
        for char in s:
            if char in countDic:
                countDic[char] += 1
            else:
                countDic[char] = 1
        for char in t:
            if char not in countDic:
                return False
            else:
                countDic[char] -= 1
        for char in countDic:
            if countDic[char] != 0:
                return False
        return True

solu = Solution()
print(solu.isAnagram1('anagram','nangram'))
print(solu.isAnagram1('anagram','naagram'))