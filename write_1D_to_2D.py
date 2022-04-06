# converts 1-D input data to 2-D

onedim = input('Name 1-D file in data directory (no file extension):')

onedimin = open('data/' + onedim +'.txt', 'r')
twodimin = open('data/' + onedim +'_2D.txt', 'w')

def x_to_index(x):
    return round(float(x) * 20)

def y_to_index(y):
    return round(float(y) * 11)

def onedimarray_string(array):
    result = ''
    for i in range(len(array)):
        result += str(array[i]) + ' '
    return result

while True:
    one_line = onedimin.readline()
    if not one_line:
        break
    one_array = one_line.split()

    two_array = [0.0 for i in range(220)]

    currX = x_to_index(one_array[220])
    currY = y_to_index(one_array[221])
    goalX = x_to_index(one_array[222])
    goalY = y_to_index(one_array[223])

    array_index = 0
    for j in range(11):
        for i in range(20):
            if currX == i and currY == j: #if this is player position
                two_array[array_index] = 0.66
                #print(i, j, array_index)
            elif goalX == i and goalY == j: #if this is goal position
                two_array[array_index] = 1.0
                #print(i,j, array_index)
            elif one_array[array_index] == '0': #if this was originally empty space
                two_array[array_index] = 0.0
            elif one_array[array_index] == '1': #if this was original full space
                two_array[array_index] = 0.33
            array_index += 1
    twodimin.write(onedimarray_string(two_array) + '\n')