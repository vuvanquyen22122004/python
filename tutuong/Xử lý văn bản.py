import re
import sys
n = sys.stdin.read().strip()
d = re.split(r"[.?!]", n)
for c in d:
    c = c.strip()
    if c:

        words = c.split()
        c = " ".join(words)
        c = c.lower()
        c = c[0].upper() + c[1:]

        print(c)
