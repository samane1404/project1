import login, register
import logging

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

print()
print("********** WELCOME **********")
while True:
    try:
        m = int(input('1. Register \n2. Login to account \n3. Exit \nselect number of your choice: '))
        break
    except ValueError:
        print()
        print('((((((((((Error! this is not number!))))))))))')
        continue

while m != 3:
    if m == 1:
        while True:
            try:
                n = int(input("1. student or 2. education responsible or 3. back : "))
                break
            except ValueError:
                print()
                print('((((((((((Error! this is not number!))))))))))')
                continue
        while n != 3:
            if n == 1:
                logging.info('One person intends to register as a student! ')
                register.RegisterStudent(n).input1()
            elif n == 2:
                logging.info('One person intends to register as a education responsible! ')
                register.RegisterEducationResponsible(n).input2()
            else:
                print('\n((((((((((Error! this number is not correct!))))))))))')
            n = int(input("1. student or 2. education responsible or 3. back : "))
    elif m == 2:
        while True:
            try:
                n = int(input("1. student or 2. education responsible or 3. back : "))
                break
            except ValueError:
                print()
                print('((((((((((Error! this is not number!))))))))))')
                continue
        while n != 3:
            if n == 0:
                print('\n((((((((((Error! this number is not correct!))))))))))')
            elif n == 1:
                logging.info('One person intends to login as a student! ')
                login.LoginStudent(n).input1()
            elif n == 2:
                logging.info('One person intends to login as a education responsible! ')
                login.LoginEducationResponsible(n).input2()
            else:
                print('\n((((((((((Error! this number is not correct!))))))))))')
            n = int(input("1. student or 2. education responsible or 3. back : "))
    else:
        print('\n((((((((((Error! this number is not correct!))))))))))')
    m = int(input("\n1. Register \n2. Login to account \n3. Exit \nselect number of your choice: "))
