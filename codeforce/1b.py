import re

f = lambda x : 26 ** x

def convert(s):
    reg = re.match(r'R(\d+)C(\d+)',s)
    if reg:
        row = reg.group(1)
        col = int(reg.group(2))

        while col:
            row = chr((col-1)%26 + ord('A'))+row
            col = (col-1)/26
    else:
        reg = re.match(r'(\D+)(\d+)',s)
        row = 'R' + reg.group(2) + 'C'
        col = 0
        for x in reg.group(1):
            col = col*26 + ord(x)-ord('A')+1
        row += str(col)
    print row


if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        s = raw_input().rstrip()
        convert(s)
