import pywhatkit
wno = input('what no: ')
msg = input('message: ')
hr = int(input('Hour(24 hours format): '))
mnt =  int(input('Minutes: '))
pywhatkit.sendwhatmsg('+91'+ wt, msg, hr, mnt)