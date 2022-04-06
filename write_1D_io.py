import numpy as np

def getdir_array(dir):
    #process dash
    dashArray = [0,0,0,0] #U D L R
    if dir == 'U':
        dashArray[0] = 1
    elif dir == 'D':
        dashArray[1] = 1
    elif dir == 'L':
        dashArray[2] = 1
    elif dir == 'R':
        dashArray[3] = 1
    elif dir == 'UL':
        dashArray[0] = 1
        dashArray[2] = 1
    elif dir == 'UR':
        dashArray[0] = 1
        dashArray[3] = 1
    elif dir == 'DL':
        dashArray[1] = 1
        dashArray[2] = 1
    elif dir == 'DR':
        dashArray[1] = 1
        dashArray[3] = 1
    else:
        return -1
    return dashArray

def printMatrix(matrix, reformat):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            charToPrint = ''
            origChar = matrix[i][j]
            if reformat:
                if origChar == '0':
                    charToPrint = '.'
                elif origChar == '1':
                    charToPrint = 'X'
                elif origChar == 'X':
                    charToPrint = 'O'
                else:
                    charToPrint = origChar
            else:
                charToPrint = origChar
            print(charToPrint, end=' ')
        print('')
    print()

levelsdir = input('Name an existing levels file in data directory (no file extension):')

levels = open('data/' + levelsdir + '.txt', 'r')

resultdir = input('Give a filename for the resulting input and output files. The files created will be in the form: <input>_in.txt and <input>_out.txt')
testin = open('data/' + resultdir + 'in.txt', 'w')
testout = open('data/' + resultdir + 'out.txt', 'w')

while True:
    this_line = levels.readline()
    if not this_line:
        break
    print('starting ' + levels.readline())

    levelvector = np.array([])
    levelmatrix = np.zeros((0,20))
    for j in range(11):
        gridline = levels.readline()
        vector = gridline.split()
        levelvector = np.append(levelvector, vector)
        levelmatrix = np.append(levelmatrix,[vector], axis=0)
    current = levels.readline().split()
    target = levels.readline().split()

    #levelvector = np.append(levelvector, current) don't actually want to add current yet
    #levelvector = np.append(levelvector, target) target and bias will get added after real current is added
    #levelvector = np.append(levelvector, [1])
    #print(levelvector.shape)
    #print(levelmatrix)

    #levelvector is to be printed as a single line to testin
    #levelmatrix is ideal for using sim_dash() (not necessarily useful in the file writing)

    for inner_i in range(levelmatrix.shape[0]):
        for j in range(levelmatrix.shape[1]):
            tempmatrix = np.copy(levelmatrix)
            tempmatrix[int(target[1])][int(target[0])] = 'G'
            if tempmatrix[inner_i][j] == '0':
                tempmatrix[inner_i][j] = 'X'
                printMatrix(tempmatrix, True)
                print('x:', j, 'y:', inner_i)
                input_valid = False

                if ((int(target[0]), int(target[1])) == (j, inner_i)):
                    print('goal found, matrix skipped')
                    input_valid = True
                
                while(not input_valid):
                    user_input = input('Choose direction, skip() if impossible to reach, exit() to exit:')
                    if user_input == 'exit()':
                        raise Exception('Program terminated by user')

                    dashArray = getdir_array(user_input)
                    if user_input == 'skip()':
                        print('skipped by user')
                        input_valid = True
                    elif dashArray == -1:
                        print('invalid direction inputted, try again')
                    else:
                        levelvectorwdash = np.copy(levelvector)
                        levelvectorwdash = np.append(levelvectorwdash, [int(j)/20, int(inner_i)/11, int(target[0])/20, int(target[1])/11, 1])

                        vectorOutput = ''
                        for v in range(levelvectorwdash.shape[0]):
                            vectorOutput += str(levelvectorwdash[v] + ' ')
                        testin.write(vectorOutput.strip() + '\n')

                        #writing the dash in four directions to the output file
                        dashOutput = ''
                        for f in range(4):
                            dashOutput += str(dashArray[f]) + ' '
                        testout.write(dashOutput.strip()+ '\n')

                        input_valid = True
                

    