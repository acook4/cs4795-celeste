# writes an output file with four outputs to a file with eight outputs

def four_to_eight(fourvec):
    eightvec = [0 for i in range(8)]
    if fourvec[0] and fourvec[2]:
        eightvec[4] = 1
    elif fourvec[0] and fourvec[3]:
        eightvec[5] = 1
    elif fourvec[1] and fourvec[2]:
        eightvec[6] = 1
    elif fourvec[1] and fourvec[3]:
        eightvec[7] = 1
    elif fourvec[0]:
        eightvec[0] = 1
    elif fourvec[1]:
        eightvec[1] = 1
    elif fourvec[2]:
        eightvec[2] = 1
    elif fourvec[3]:
        eightvec[3] = 1
    return eightvec

userinput = input('Enter existing output file name (do not include file extension):')
fourvecfile = open('data/' + userinput + '.txt', 'r')
eightvecfile = open('data/' + userinput + '_8.txt', 'w')

while True:
    line = fourvecfile.readline()    
    if not line:
        break
    fourvec = [int(i) for i in line.split()]
    eightvec = four_to_eight(fourvec)

    dashOutput = ''
    for f in range(8):
        dashOutput += str(eightvec[f]) + ' '
    eightvecfile.write(dashOutput.strip() + '\n')