from time import sleep
from datetime import datetime

success = []
while 1:
    dateSTR = datetime.now().strftime('%H:%M')
    if (dateSTR) == (newnametest) and not dateSTR in done:
        done.append(dateSTR)
        os.system("mplayer -ao alsa:device=bluealsa /home/pi/test.mp3")
    print(dateSTR)
