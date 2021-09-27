import csv
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class LoginStudent:
    def __init__(self, n, file='text.csv'):
        self.n = n
        self.file = file
        self.use_student = None
        self.pass_student = None
        self.pass_student_again = None


    def input1(self):
        self.use_student = input("Enter username: ")
        self.pass_student = input("Enter password: ")
        list1 = []
        list2 = []
        with open('text.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list1.append(row['username:'])
                list2.append(row['password:'])
        while True:
            try:
                if self.use_student not in list1:
                    raise ValueError('((((((((((Error! enter correct username!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong username for logging in as a student ! ')
                print(error)
                self.use_student = input("Enter username: ")
        while True:
            try:
                if self.pass_student not in list2:
                    raise ValueError('((((((((((Error! enter correct password!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for logging in as a student ! ')
                print(error)
                self.pass_student = input("Enter password: ")

        while True:
            try:
                k = int(input("1. show lessons or 2. search or 3. total units or 4. back : "))
                break
            except ValueError:
                print()
                print('((((((((((Error! this is not number!))))))))))')
                continue
        logging.info('One person successfully log in as student! ')
        while k != 4:
            if k == 1:
                with open('lesson.csv', "r") as f:
                    reader = csv.reader(f, delimiter=",", quotechar='|')
                    for row in reader:
                        print(', '.join(row))
            elif k == 2:
                list3 = []
                list5 = []
                with open("lesson.csv", 'r') as f:
                    csv_reader = csv.reader(f)
                    rows = list(csv_reader)
                    for i in rows:
                        list3.append(i[0])
                        list5.append(i[1])
                    print(list3)
                    p = input("which one? or back? ")
                    while p != 'back':
                        if p in list3:
                            print(rows[list3.index(p)])
                        else:
                            print('\n((((((((((Error! this word is not correct!))))))))))')
                        p = input("which one? or back? ")
            elif k == 3:
                df2 = pd.read_csv('lesson.csv')
                df2['units:'].sum()
                print(df2['units:'].sum())
            else:
                print('\n((((((((((Error! this number is not correct!))))))))))')
            k = int(input("1. show lessons or 2. search or 3. total units or 4. back : "))

class LoginEducationResponsible:
    def __init__(self, n, file='textt.csv'):
        self.n = n
        self.file = file
        self.use_responsible = None
        self.pass_responsible = None
        self.pass_responsible_again = None

    def input2(self):
        self.use_responsible = input("Enter username: ")
        self.pass_responsible = input("Enter password: ")
        list1 = []
        list2 = []
        with open('textt.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list1.append(row['username:'])
                list2.append(row['password:'])
        while True:
            try:
                if self.use_responsible not in list1:
                    raise ValueError('((((((((((Error! enter correct username!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong username for logging in as a education responsible! ')
                print(error)
                self.use_responsible = input("Enter username: ")
        while True:
            try:
                if self.pass_responsible not in list2:
                    raise ValueError('((((((((((Error! enter correct password!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for logging in as a education responsible! ')
                print(error)
                self.pass_responsible = input("Enter password: ")

        while True:
            try:
                k = int(input("1. show lessons or 2. search or 3. total units or 4. define a lesson or 5.back: "))
                break
            except ValueError:
                print()
                print('((((((((((Error! this is not number!))))))))))')
                continue
        logging.info('One person successfully log in as education responsible! ')
        while k != 5:
            if k == 1:
                with open('lesson.csv', "r") as f:
                    reader = csv.reader(f, delimiter=",", quotechar='|')
                    for row in reader:
                        print(', '.join(row))
            elif k == 2:
                list3 = []
                with open("lesson.csv", 'r') as f:
                    csv_reader = csv.reader(f)
                    rows = list(csv_reader)
                    for i in rows:
                        list3.append(i[0])
                    print(list3)
                    p = input("which one? or back? ")
                    while p != 'back':
                        if p in list3:
                            print(rows[list3.index(p)])
                        else:
                            print('\n((((((((((Error! this word is not correct!))))))))))')
                        p = input("which one? or back? ")
            elif k == 3:
                df2 = pd.read_csv('lesson.csv')
                df2['units:'].sum()
                print(df2['units:'].sum())
            elif k == 4 :
                les = input("lesson: ")
                list4 = []
                with open('lesson.csv', 'r') as myfile:
                    reader = csv.DictReader(myfile)
                    for row in reader:
                        list4.append(row['lesson:'])
                while True:
                    try:
                        if les in list4:
                            raise ValueError('((((((((((Error! this lesson exist!))))))))))')
                        break
                    except ValueError as error:
                        logging.info('education responsible entered duplicate lesson! ')
                        print(error)
                        les = input("Enter another lesson: ")
                uni = input("units: ")
                cap = input("capacity: ")
                r_cap = input("remain_capacity: ")
                with open('lesson.csv', 'a', newline='') as f:
                    write = csv.DictWriter(f, fieldnames=['lesson:', 'units:', 'capacity:', 'remain_capacity:'])
                    if f.tell() == 0:
                        write.writeheader()
                    write.writerows(
                        [{'lesson:': les, 'units:': uni, 'capacity:': cap, 'remain_capacity:': r_cap}])
                    logging.info('education responsible entered new lesson! ')
            else:
                print('\n((((((((((Error! this number is not correct!))))))))))')
            k = int(input("1. show lessons or 2. search or 3. total units or 4. define a lesson or 5.back: "))
