def convert(tstr, addsec):
    sec=int(tstr[-2:])
    mins=int(tstr[-5:-3])
    hrs=int(tstr[-8:-6])
    sec=sec+addsec
    mins=mins+(sec/60)
    sec=sec%60
    hrs=hrs+(mins/60)
    mins=mins%60
    return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(sec).zfill(2)


import re
import sys
filename=sys.argv[1]
addsec=int(sys.argv[2])
f=open(filename)
text=f.read()
times=re.findall('[0-9]+:[0-9]+:[0-9]+',text)
timesnew=[]
for i in times:
    timesnew.append(convert(i, addsec))

for i in range(len(times)):
    text=text.replace(times[i],timesnew[i])


f.close()

f=open(filename, 'w')
f.write(text)
f.close()
