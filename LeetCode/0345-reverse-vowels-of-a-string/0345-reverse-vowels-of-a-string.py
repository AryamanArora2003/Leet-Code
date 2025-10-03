class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set(["a","e","i","o","u","A","E","I","O","U"])

        vowString=""

        for letter in s:
            if letter in vowels:
                vowString += letter 

        listS = list(s)
        for letter in range(len(s)):
            if listS[letter] in vowels:
                listS[letter] = vowString[-1]
                vowString = vowString[:-1]

        s = ''.join(listS)


        return s

