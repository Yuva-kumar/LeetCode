class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(' ')
        
        if len(s) != len(pattern):
            return False

        dict = {}
        for i in range(len(pattern)):

            if pattern[i] not in dict:
                dict[pattern[i]] = s[i]
            else:
                if dict[pattern[i]] != s[i] :
                    return False
        if len(list(dict.values())) != len(list(set(dict.values()))):
            return False
        return True

