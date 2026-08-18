class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] =  count1.get(c,0)+1
        
        left = 0
        window = {}

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0)+1
            if right-left+1> len(s1):
                window[s2[left]] -=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if window == count1:
                return True
        return False
                
                


        

        