import sys
import time
from modules.sevseg import getSevSegStr

try:
    while True:
        print('\n' * 20)

        current_time = time.localtime()
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)
        print(hours, minutes, seconds)
        hDigits = getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()

        print('Press Ctrl+C to quit.')

        while True:
            time.sleep(0.8)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock')
    sys.exit()
