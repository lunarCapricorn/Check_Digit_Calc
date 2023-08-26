import os
import coreCounting
os.system('clear')

# User chooses between reading from file or typing the digits manually
choice = input('Type in values[0] or read from file "values.txt"[1]? >> ')
if ((choice is not '0') and (choice is not '1')):
    print(f'''
{choice} is not a valid input.
Only valid inputs: 
* Type in values ---> 0
* Read from file "values.txt" ---> 1
''')
else:
    if (choice == '0'):
        data = input('What digits? >> ')
        data_list = [x for x in data.lower()]
        coreCounting.switch(data_list)
    else:
        values_file = open('values.txt', 'r+')
        data = values_file.read()
        values_file.close()
        data_list = [x for x in data.lower()]
        print(data_list)
        coreCounting.switch(data_list)