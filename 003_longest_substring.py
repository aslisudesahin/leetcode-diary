class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        viewed_char = {}
        start=0
        longest_subs=""

        for end, char in enumerate(s):
          if char in viewed_char and viewed_char[char]>=start:
            start= viewed_char[char] +1 

          current_string= s[start:end+1]
          if len(current_string)>=len(longest_subs):
             longest_subs=current_string
         
          viewed_char[char]=end
  
        return len(longest_subs) 
