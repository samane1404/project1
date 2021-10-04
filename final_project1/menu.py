import logging
import signup
from signin_student import Student
from signin_teacher import Teacher
from signin_education_responsible import EducationResponsible

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
print()
print('******************** WELCOME ********************')
while True:
    try:
        m = int(input('1. sign up \n2. sign in \n3. Exit \nselect number of your choice: '))
        print()
        break
    except ValueError:
        print()
        print('<<<<<<<<<< Error! this is not a number! >>>>>>>>>>')
        logging.error('One person enter not valid key! ')
        continue
while m != 3:
    if m == 1:
        while True:
            try:
                n = int(input('1. student \n2. teacher \n3. education responsible \n4. back \nselect number of your choice: '))
                print()
                break
            except ValueError:
                print()
                print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                logging.error('One person enter not valid key! ')
                continue
        while n != 4:
            if n == 1:
                signup.student()
                logging.info('One person intends to register as a student! ')
            elif n == 2:
                signup.teacher()
                logging.info('One person intends to register as a teacher! ')
            elif n == 3:
                signup.education_responsible()
                logging.info('One person intends to register as a education responsible! ')
            else:
                print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
                logging.error('One person enter not valid key! ')
            while True:
                try:
                    n = int(input(
                        '1. student \n2. teacher \n3. education responsible \n4. back \nselect number of your choice: '))
                    print()
                    break
                except ValueError:
                    print()
                    print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                    logging.error('One person enter not valid key! ')
                    continue
            print()
    elif m == 2:
        while True:
            try:
                n = int(input('1. student \n2. teacher \n3. education responsible \n4. back \nselect number of your choice: '))
                print()
                break
            except ValueError:
                print()
                print('<<<<<<<<<< Error! this is not number!>>>>>>>>>>')
                logging.error('One person enter not valid key! ')
                continue
        while n != 4:
            if n == 1:
                s = Student()
                s.login()
                logging.info('One person intends to login as a student! ')
            elif n == 2:
                t = Teacher()
                t.login()
                logging.info('One person intends to login as a teacher! ')
            elif n == 3:
                e = EducationResponsible()
                e.login()
                logging.info('One person intends to login as a education responsible! ')
            else:
                print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
                logging.error('One person enter not valid key! ')
            while True:
                try:
                    n = int(input(
                        '1. student \n2. teacher \n3. education responsible \n4. back \nselect number of your choice: '))
                    print()
                    break
                except ValueError:
                    print()
                    print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                    logging.error('One person enter not valid key! ')
                    continue
            print()
    else:
        print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
        logging.error('One person enter not valid key! ')
    while True:
        try:
            m = int(input("\n1. sign up \n2. sign in \n3. Exit \nselect number of your choice: "))
            print()
            break
        except ValueError:
            print()
            print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
            logging.error('One person enter not valid key! ')
            continue
    print('******************** Process finished successfully ********************')


