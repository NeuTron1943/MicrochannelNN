#!/home/roudnev/python38/bin/python
import sys
import re
print(sys.argv[1])
with open(sys.argv[1],'r') as f:
    with open(sys.argv[2], 'w') as out:
        for l in f.readlines():
            s=l.strip()
            s=re.sub(r'([0-9])-([0-9])',r'\1 -\2',s)
            # print(s)
            out.write(s + '\n')
out.close()