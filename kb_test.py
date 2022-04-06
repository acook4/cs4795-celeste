import keyboard
import time

def dash(dir):
    print('dash ' + str(dir))
    if dir == 'L':
        keyboard.press('a+x')
        time.sleep(0.1)
        keyboard.release('a+x')
    elif dir == 'R':
        keyboard.press('d+x')
        time.sleep(0.1)
        keyboard.release('d+x')
    elif dir == 'U':
        keyboard.press('w+x')
        time.sleep(0.1)
        keyboard.release('w+x')
    elif dir == 'D':
        keyboard.press('s+x')
        time.sleep(0.1)
        keyboard.release('s+x')
    elif dir == 'UL':
        keyboard.press('w+a+x')
        time.sleep(0.1)
        keyboard.release('w+a+x')
    elif dir == 'UR':
        keyboard.press('w+d+x')
        time.sleep(0.1)
        keyboard.release('w+d+x')
    elif dir == 'DL':
        keyboard.press('s+a+x')
        time.sleep(0.1)
        keyboard.release('s+a+x')
    elif dir == 'DR':
        keyboard.press('s+d+x')
        time.sleep(0.1)
        keyboard.release('s+d+x')
    else:
        print('error, invalid dash path ' + str(dir))
    time.sleep(0.2)

def main():

    time.sleep(5)

    #input a sequence of dash() calls to beat the level

    keyboard.unhook_all()
    print('success')

if __name__ == '__main__':
    main()