import re
a="vu,:van?quyen"
for i in re.split("[" ",:?]",a):
    print(i)