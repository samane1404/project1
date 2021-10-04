import csv
import logging
import pandas as pd


logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class Student:
    def __init__(self):
        self.use_student = None
        self.pas_student = None
        self.fname = None
        self.lname = None

    def login(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        with open('student.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list1.append(row['username:'])
                list2.append(row['password:'])
                list3.append(row['first_name:'])
                list4.append(row['last_name:'])
        self.use_student = input('Enter username: ')
        while True:
            try:
                if self.use_student not in list1:
                    raise ValueError('<<<<<<<<<< Error! enter correct username! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong username for logging in as a student ! ')
                print(error)
                self.use_student = input('Enter username: ')
        self.pas_student = input('Enter password: ')
        while True:
            try:
                if self.pas_student not in list2:
                    raise ValueError('<<<<<<<<<< Error! enter correct password! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for logging in as a student ! ')
                print(error)
                self.pas_student = input('Enter password: ')
        self.fname = list3[list1.index(self.use_student)]
        self.lname = list4[list1.index(self.use_student)]
        Student.menu(self)

    def menu(self):
        logging.info('One person successfully log in as student! ')
        while True:
            try:
                print()
                print(f'******************** Hi {self.fname} {self.lname} ********************')
                k = int(
                    input('1. show list of courses \n2. search course by name \n3. show total units \n4. select course '
                          '\n5. show result of unit selection \n6. back \nselect number of your choice:  '))
                break
            except ValueError:
                print()
                print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                continue
        while k != 6:
            if k == 1:
                Student.show_all_courses(self)
            elif k == 2:
                Student.search_by_course_name(self)
            elif k == 3:
                Student.total_units(self)
            elif k == 4:
                Student.select_course(self)
            elif k == 5:
                Student.show_result(self)
            else:
                print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
            while True:
                try:
                    print()
                    print(f'******************** Hi {self.fname} {self.lname} ********************')
                    k = int(
                        input(
                            '1. show list of courses \n2. search course by name \n3. show total units \n4. select course '
                            '\n5. show result of unit selection \n6. back \nselect number of your choice:  '))
                    break
                except ValueError:
                    print()
                    print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                    continue

    def show_all_courses(self):
        df = pd.read_csv("course.csv")
        print(df)
        print('-' * 50)
        print()

    def search_by_course_name(self):
        list3 = []
        with open("course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list3.append(i[0])
            print()
            print(list3)
            p = input("Enter name of course or back : ")
            while p != 'back':
                if p in list3:
                    print()
                    e = tuple(rows[list3.index(p)])
                    j = tuple(rows[0])
                    print(list(zip(j,e)))
                else:
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                p = input("Enter name of course or back : ")
        print('-' * 50)
        print()

    def total_units(self):
        df2 = pd.read_csv('course.csv')
        df2['units:'].sum()
        print('-' * 50)
        print('total units = ' , df2['units:'].sum())
        print('-' * 50)
        print()

    def select_course(self):
        list6 = []
        with open('student_course.csv', 'r') as g:
            csv_reader = csv.reader(g)
            rows = list(csv_reader)
            for j in rows:
                list6.append(j[0])
            if self.use_student not in list6:
                list1 = [self.use_student]
                list3 = []
                list2 = []
                with open("course.csv", 'r') as f:
                    csv_reader = csv.reader(f)
                    rows = list(csv_reader)
                    for i in rows:
                        list3.append(i[0])
                        list2.append(i[1])
                    unit = 0
                    while unit < 17 :
                        print()
                        print(list3)
                        p = input(" Enter name of course : ")
                        while p not in list3:
                            print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                            p = input(" Enter name of course : ")
                        capacity = int(rows[list3.index(p)][3])
                        if capacity >= 1:
                            list1.append(p)
                            unit = unit + int(rows[list3.index(p)][1])
                            ls = open('course.csv', 'r')
                            reader = csv.reader(ls)
                            myls = list(reader)
                            ls.close()
                            myls[list3.index(p)][3] = int(rows[list3.index(p)][3])-1
                            my_new_list = open('course.csv', 'w', newline='')
                            csv_writer = csv.writer(my_new_list)
                            csv_writer.writerows(myls)
                            my_new_list.close()
                            print(' This unit was successfully selected! ')
                            print()
                        else:
                            print(' Capacity is full! ')
                            print()
                    # list1.append(unit)
                    with open('student_course.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow(list1)
            else:
                print()
                logging.warning('a person do select unit as a student ! ')
                print(' You have done it befor! ')
                print('-' * 50)
                print()

    def show_result(self):
        list3 = []
        with open("student_course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list3.append(i[0])
            try:
                p = tuple(rows[list3.index(self.use_student)])
                print()
                # print('\'your name\'' ,', ' , '\'courses_1 ...\'' ,', ' , '\'total units\'')
                print(p)
                # l = tuple(rows[list3.index('username:')])
                # print(list(zip(l,p)))
            except ValueError:
                print()
                print('<<<<<<<<<< Error! First select courses! >>>>>>>>>>')
        print('-' * 50)
        print()


