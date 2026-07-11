class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral to its corresponding integer value
        roman = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            curr = roman[s[i]]
            # If there's a next character, get its value; otherwise, it's 0
            next_val = roman[s[i + 1]] if i + 1 < n else 0
            
            # If the current value is less than the next value, subtract it
            # (e.g., IV -> subtract 1, add 5 = 4)
            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result