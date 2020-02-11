"""
title: 171 Excel
date: Feb/11,2020
author: tom8u4286
Difficulty: easy
"""

class Solution:
    def titleToNumber(self, s:str) -> int:
        
        sum = 0
        for idx, i in enumerate(list(s)):
            sum += math.pow(26,len(s)-1-idx)*(ord(i)-64)
        
        return int(sum)

