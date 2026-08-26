class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict={}
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            if key not in anagram_dict:
                anagram_dict[key]=[]
            anagram_dict[key].append(s)
        return anagram_dict.values()