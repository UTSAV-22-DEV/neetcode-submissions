class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l,r=0,0
        maxlen=0
        mp={}
        maxfr=0
        changes=0
        while r<n:
            mp[s[r]]=mp.get(s[r],0)+1
            maxfr=max(maxfr,mp[s[r]])
            changes=(r-l+1)-maxfr
            if changes<=k:
                maxlen=max(maxlen,r-l+1)
            else:
                mp[s[l]]-=1
                l+=1
                changes=0
            r+=1
        return maxlen                         