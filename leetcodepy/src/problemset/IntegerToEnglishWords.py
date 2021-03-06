'''
Created on Sep 20, 2015

@author: mianmianba
'''

class NumberToWords(object):
    def under1000(self, num):
        if num == 0: return "Zero"
        belowTwenty = ["Zero", "One", "Two", "Three", "Four", "Five", 
                       "Six", "Seven", "Eight", "Nine", "Ten", 
                       "Eleven", "Twelve", "Thirteen", "Fourteen",
                       "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        tenth = ["Zero", "Ten", "Twenty", "Thirty", "Forty", 
                 "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        hundreds = num/100
        numStr = ""
        if hundreds != 0:
            numStr = (belowTwenty[hundreds] + " Hundred")
            num -= 100*hundreds
        if num == 0:
            return numStr
        elif num < 20:
            if numStr: numStr += " "
            numStr += belowTwenty[num]
        else:
            if numStr: numStr += " "
            numStr += tenth[num/10]
            if num%10 != 0:
                numStr += (" " + belowTwenty[num%10])
        return numStr
        
    def solution(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        belowTwenty = ["Zero", "One", "Two", "Three", "Four", "Five", 
                       "Six", "Seven", "Eight", "Nine", "Ten", 
                       "Eleven", "Twelve", "Thirteen", "Fourteen",
                       "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        numStr = ""
        billion = num / 1000000000
        if billion != 0:
            numStr = belowTwenty[billion] + " Billion";
            num -= 1000000000*billion
        million = num / 1000000
        if million != 0:
            milStr = self.under1000(million) + " Million"
            if numStr: numStr += (" " + milStr)
            else:
                numStr = milStr
            num -= 1000000*million
        thousand = num / 1000
        if thousand != 0:
            thouStr = self.under1000(thousand) + " Thousand"
            if numStr: numStr += (" " + thouStr)
            else:
                numStr = thouStr
            num -= 1000*thousand
        if num != 0:
            if numStr: numStr += (" " + self.under1000(num))
            else:
                numStr = self.under1000(num)
        return numStr
    
            
