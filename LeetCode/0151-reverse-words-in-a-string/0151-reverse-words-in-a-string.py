class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []

        while s != "":
            tempstr = ""
            for char in s:
                if char == " ":
                    s = s[len(tempstr) + 1:].lstrip()
                    words.append(tempstr)  
                    break
                else:
                    tempstr += char
            else:
                # no space found -> last word
                words.append(tempstr)
                s = ""


        retstr = ""
        for vocab in reversed(words):
            retstr += vocab
            retstr += " "

        return retstr[:-1].lstrip()
