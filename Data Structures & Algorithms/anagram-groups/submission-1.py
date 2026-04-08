class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newhash = {}
        for i in strs:
            sort_words = ''.join(sorted(i))
            if sort_words not in newhash:
                newhash[sort_words] = []
            newhash[sort_words].append(i)
        result = list(newhash.values())
        return result        
       
            

