class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            if ch not in count:
                return False
            else:
                if count[ch]==0:
                    return False
                else:
                    count[ch]-=1
        return True
        