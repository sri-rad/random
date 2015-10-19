def convert(tstr, addsec):
    try:
        print tstr[-2:]
        sec=int(tstr[-2:])
        mins=int(tstr[-5:-3])
        hrs=int(tstr[-8:-6])
        sec=sec+addsec
        mins=mins+(sec/60)
        sec=sec%60
        hrs=hrs+(mins/60)
        mins=mins%60
        return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(sec).zfill(2)
    except ValueError:
        return tstr
    
import re
import sys
filename=sys.argv[1]
addsec=int(sys.argv[2])
f=open(filename)
text=f.read()
times=re.findall('[0-9]+:[0-9]+:[0-9]+,[0-9]+',text)
print times[0][:-4]
timesnew=[]
for i in times:
    timesnew.append(convert(i[:-4], addsec)+i[-4:])
print '[',
for i in range(len(times)):
    print '=',
    text=text.replace(times[i],timesnew[i])


f.close()
f=open(filename, 'w')
f.write(text)
f.close()
