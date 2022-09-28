def canConstruct( ransomNote, magazine):
        table = dict()
        
        for i in range(len(magazine)):
            letter = magazine[i]
            if letter in table:
                table[letter] +=1
            else:
                table[letter] = 1
        sum = 0
        for i in range(len(ransomNote)):
            letter = ransomNote[i]
            
            if letter in table:
                if table[letter]==1:
                    sum+=1
                    table.pop(letter)
                else:
                    table[letter]-=1
                    sum+=1
        if sum!=len(ransomNote):
            return False
        return True

print(canConstruct("aa","ab"))