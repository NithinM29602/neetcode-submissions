class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for eachStr in strs:
            sortedStr = ''.join(sorted(eachStr))
            anagramDict[sortedStr] = anagramDict[sortedStr] + [eachStr]

        anagramSublist = []
        for value in anagramDict.values():
            anagramSublist.append(value)
        
        return anagramSublist

        