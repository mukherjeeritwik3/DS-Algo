#LeetCode problem - Medium
def RomanToInt(s):
        """
        :type num: int
        :rtype: str
        """
        dicts = {'I'     :        1,
                'V'      :       5,
                'X'      :      10,
                'L'      :       50,
                'C'      :       100,
                'D'      :       500,
                'M'      :       1000}

        leng = len(s)
        idx = 0
        sum = 0
        while(idx!=leng):
                if(idx+1==leng):
                                sum+=dicts.get(s[idx])
                                idx+=1
                                continue

                if (s[idx]=="C"):
                        
                        

                        if(s[idx+1]=="M"):
                                temp = dicts.get("M") - dicts.get("C")
                                sum+=temp
                                idx+=2
                                continue
                        if(s[idx+1]=="D"):
                                temp = dicts.get("D") - dicts.get("C")
                                sum+=temp
                                idx+=2
                                continue
                if (s[idx]=="X"):
                        if(s[idx+1]=="L"):
                                temp = dicts.get("L") - dicts.get("X")
                                sum+=temp
                                idx+=2
                                continue
                        if(s[idx+1]=="C"):
                                temp = dicts.get("C") - dicts.get("X")
                                sum+=temp
                                idx+=2
                                continue
                if (s[idx]=="I"):
                        if(s[idx+1]=="V"):
                                temp = dicts.get("V") - dicts.get("I")
                                sum+=temp
                                idx+=2
                                continue
                        if(s[idx+1]=="X"):
                                temp = dicts.get("X") - dicts.get("I")
                                sum+=temp
                                idx+=2
                                continue        
                
                sum+=dicts.get(s[idx])
                idx+=1
        return sum

s = "LVIII      "
print(RomanToInt(s))
