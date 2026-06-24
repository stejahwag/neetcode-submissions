class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_dict = defaultdict(list)
        
        for word in strs:
            char_freq = {}

            for i in range(len(word)):
                char_freq[word[i]] = 1 + char_freq.get(word[i], 0)

            fingerprint = tuple(sorted(char_freq.items()))

            master_dict[fingerprint].append(word)

        return list(master_dict.values())