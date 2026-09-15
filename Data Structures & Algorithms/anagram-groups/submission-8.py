class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for eachStr in strs:
            char = [0] * 26
            for eachChar in eachStr:
                charPos = ord(eachChar) - ord('a')
                char[charPos] += 1

            anagramDict[tuple(char)].append(eachStr)

        anagramSublist = []
        for value in anagramDict.values():
            anagramSublist.append(value)
        
        return anagramSublist
            

        