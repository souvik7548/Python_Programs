import re
count=0
pattern=re.compile('ab')
matcher=re.finditer(pattern,'abaababa')
for match in matcher:
    count+=1
    print('Match Is Available At Start Index',match.start())
print('The Count Of The Pattern Is In Data',count)
