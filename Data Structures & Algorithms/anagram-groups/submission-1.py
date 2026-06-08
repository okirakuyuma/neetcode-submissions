class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in range(len(strs)):
            srt_sorted=sorted(strs[i])
            srt_sorted="".join(srt_sorted)
            if srt_sorted not in seen:
                seen[srt_sorted]=[]
            seen[srt_sorted].append(strs[i])
        return list(seen.values())