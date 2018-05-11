import os
import random
import time
import requests
from appetizer import Appetizer


ip_addr = '129.122.181.156:5555'
cmd_1 = 'adb kill-server'
cmd_2 = 'adb start-server'
cmd_3 = 'adb tcpip 5555'
cmd_4 = 'adb connect ' + ip_addr
counter = 0


appetizer = Appetizer(toolkit='C:\\TMP\\replaykit\\win32\\appetizer.exe')

print("Is it first time you start the app? 1 - Yes, 0 - No")
answer = ''
while answer != '1' or answer != '0':
    answer = input()
    if answer == '1':

        done = 'Not'
        while done != '':
            print("Connect USB to PC and enable USB-debugging on the tablet")
            print("Press ENTER when it's done")
            done = input()

        # os.system(cmd_1)
        # os.system(cmd_2)
        appetizer.adb.kill_server()
        appetizer.adb.start_server()
        os.system(cmd_3)

        done = 'Not'

        while done != '':
            print("Plug-out USB cable from PC and connect the stand cable to the tablet")
            print("Press ENTER when it's done")
            done = input()

        os.system(cmd_4)
        break

    elif answer == '0':
        done = 'Not'
        while done != '':
            print("Connect the tablet and enable USB-tethering")
            print("Press ENTER when it's done")
            done = input()
        pass
        break
    else:
        print("Wrong entry")

while True:

    number = random.randint(1, 12)
    print(number)
    print("Counter: " + str(counter))

    time.sleep(30)

    print("Go!")

# Simple receipt:
    if 1 <= number <= 3:
		r = requests.get('https://pos-stg01.shtrih-cloud.ru')
		if r.status_code == 200:
			appetizer.trace.replay("C:\\TMP\\replaykit\\win32\\simple_receipt.trace", ['ip_addr', ])
			print('Ok')
			time.sleep(35)
		else:
            counter = counter + 1

    # Big receipt:
    elif 3 < number <= 6:
		r = requests.get('https://pos-stg01.shtrih-cloud.ru')
		if r.status_code == 200:
			appetizer.trace.replay("C:\\TMP\\replaykit\\win32\\complicated_receipt_12_items.trace", ['ip_addr', ])
			print('Ok')
			time.sleep(50)
		else:
            counter = counter + 1

    # Return one item:
    elif 6 < number <= 9:
        r = requests.get('https://pos-stg01.shtrih-cloud.ru')
        if r.status_code == 200:
            appetizer.trace.replay("C:\\TMP\\replaykit\\win32\\return_receipt_1_item.trace", ['ip_addr', ])
            print('Ok')
            time.sleep(40)
        else:
            counter = counter + 1

    # Return full receipt:
    elif 9 < number <= 12:
        r = requests.get('https://pos-stg01.shtrih-cloud.ru')
        if r.status_code == 200:
            appetizer.trace.replay("C:\\TMP\\replaykit\\win32\\full_return_receipt.trace", ['ip_addr', ])
            print('Ok')
            time.sleep(40)
        else:
            counter = counter + 1
