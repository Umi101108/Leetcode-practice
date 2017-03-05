"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtypr: str
        """

        ### 1st
        # l = [[] for i in range(numRows)]
        # slist = list(s)
        # j = 0

        # while slist != []:
        #     if j == 2*numRows-2:
        #         j = 0
        #     if j < numRows:
        #         l[j].append(slist[0])
        #     else:
        #         l[numRows-j%numRows-2].append(slist[0])
        #     j = j + 1
        #     slist = slist[1:]

        # zigzag = []
        # for i in range(numRows):
        #     zigzag = zigzag + l[i]
        # return ''.join(zigzag)


        ### 2nd
        if numRows <= 1: return s
        result = ''
        cycle = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                result = result + s[j]
                secondj = j - i + cycle - i
                if i!=0 and i != numRows-1 and secondj < len(s):
                    result = result + s[secondj]
        return result



s = 'PAYPALISHIRING'
numRows = 4
so = Solution()
print so.convert(s, numRows)
