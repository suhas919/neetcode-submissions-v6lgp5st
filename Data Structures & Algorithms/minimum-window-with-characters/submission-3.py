class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_arr = [0] * 128
        t_arr = [0] * 128
        need = 0
        for i in t:
            ind = ord(i)
            if t_arr[ind] == 0:
                need+=1
            t_arr[ind]+=1
        have = 0
        res = "a"*1001
        j = 0
        for i in range(len(s)):
            ind = ord(s[i])
            s_arr[ind]+=1

            if s_arr[ind] == t_arr[ind]:
                have += 1

            if need == have:
                print("i,j",i,j)
                if len(res) > (i-j+1):
                    res = s[j:i+1]
                    print("res = ",res, i-j+1)
            
            while (j < i) and (need == have):

                if len(res) > (i-j+1):
                    res = s[j:i+1]

                ind = ord(s[j])
                s_arr[ind] -= 1
                if s_arr[ind] < t_arr[ind]:
                    have -= 1
                print("moving j right")
                j+=1
            
            if need == have:
                print("i,j",i,j)
                if len(res) > (i-j+1):
                    res = s[j:i+1]
                    print("res = ",res, i-j+1)
        return res if len(res)<1001 else ""
            
        