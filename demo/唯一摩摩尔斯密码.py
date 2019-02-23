#!@Author : Sanwat
#!@File : .py
import math
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        方法一
        # Approach #2   用ord()函数求出a的ASCII值, chr() 是将ASCII值变为字符.  ord('a') = 97 ,   ord("A") = 65
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set("".join(ref[ord(s) - 97] for s in word) for word in words))
        方法二
        axb = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_a = dict(zip(axb, morse))
        temp=set()
        for i in words:
            temp_morse = []
            for j in i:
                temp_morse.append(morse_a[j])
            s = "".join(temp_morse)
            temp.add(s)
        return len(temp)
        方法三
        """
        ref = {'a':".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--.."}
        res = []
        for word in words:
            s = ''
            for i in  word:
                s+= ref.get(i)
            res.append(s)
        return len(set(res))

S=Solution()
print(S.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))