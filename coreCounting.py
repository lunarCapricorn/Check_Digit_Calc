def switch(data):
    logs = open('logs.txt', 'w')
    weight = [7,3,1]
    switches = {
        'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17, 'i':18, 'j':19,
        'k':20, 'l':21, 'm':22, 'n':23, 'o':24, 'p':25, 'q':26, 'r':27, 's':28, 't':29,
        'u':30, 'v':31, 'w':32, 'x':33, 'y':34, 'z':35, '1':1, '2':2, '3':3, '4':4, '5':5,
        '6':6, '7':7, '8':8, '9':9, '0':0, '<':0,
    }
    i = 0
    addedValues = 0
    result = 0
    for value_data in data:
        for index_base, value_base in switches.items():
            if (value_data == index_base):
                addedValues = value_base * weight[i]
                result += addedValues
                logs.write(f'{value_base} * {weight[i]} = {addedValues} >>> {result}\n')
                i += 1
                if (i >= 3): i = 0
    checkDigit = int(repr(result)[-1])
    print(f'Your check digit is >>>>> {checkDigit}')
    logs.close()