import csv
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class Teacher:
    def __init__(self):
        self.use_teacher = None
        self.pas_teacher = None
        self.fname = None
        self.lname = None

    def login(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        with open('teacher.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list1.append(row['username:'])
                list2.append(row['password:'])
                list3.append(row['first_name:'])
                list4.append(row['last_name:'])
        self.use_teacher = input('Enter username: ')
        while True:
            try:
                if self.use_teacher not in list1:
                    raise ValueError('<<<<<<<<<< Error! enter correct username! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong username for logging in as a teacher ! ')
                print(error)
                self.use_teacher = input('Enter username: ')
        self.pas_teacher = input('Enter password: ')
        while True:
            try:
                if self.pas_teacher not in list2:
                    raise ValueError('<<<<<<<<<< Error! enter correct password! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for logging in as a teacher ! ')
                print(error)
                self.pas_teacher = input('Enter password: ')
        self.fname = list3[list1.index(self.use_teacher)]
        self.lname = list4[list1.index(self.use_teacher)]
        Teacher.menu(self)

    def menu(self):
        logging.info('One person successfully log in as student! ')
        while True:
            try:
                print()
                print(f'******************** Hi {self.fname} {self.lname} ********************')
                k = int(input(
                    '1. show list of courses \n2. search course by name \n3. show list of selected courses '
                    '\n4. select course \n5. show list of student in a course \n6. back \nselect number of your choice:  '))
                break
            except ValueError:
                print()
                print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                continue
        while k != 6:
            if k == 1:
                Teacher.show_1(self)
            elif k == 2:
                Teacher.search_1(self)
            elif k == 3:
                Teacher.show_2(self)
            elif k == 4:
                Teacher.select_1(self)
            elif k == 5:
                Teacher.show_3(self)
            else:
                print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
            while True:
                try:
                    print()
                    print(f'******************** Hi {self.fname} {self.lname} ********************')
                    k = int(input(
                        '1. show list of courses \n2. search course by name \n3. show list of selected courses '
                        '\n4. select course \n5. show list of student in a course \n6. back \nselect number of your choice:  '))
                    break
                except ValueError:
                    print()
                    print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                    continue

    def show_1(self):
        df = pd.read_csv("course.csv")
        print(df)
        print('-' * 50)
        print()

    def search_1(self):
        list3 = []
        with open("course.csv", 'r') as f:
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
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                p = input("which one? or back? ")
        print('-' * 50)
        print()

    def show_2(self):
        df = pd.read_csv("course.csv")
        print(df)
        print('-' * 50)
        print()

    def select_1(self):
        list6 = []
        list7 = []
        with open('teacher_course.csv', 'r') as g:
            csv_reader = csv.reader(g)
            rows = list(csv_reader)
            for j in rows:
                list6.append(j[0])
                list7.append(j[1])
            if self.lname not in list6:
                list1 = [self.fname, self.lname]
                list3 = []
                list2 = []
                with open("course.csv", 'r') as f:
                    csv_reader = csv.reader(f)
                    rows = list(csv_reader)
                    for i in rows:
                        list3.append(i[0])
                        list2.append(i[1])
                    unit = 0
                    while unit < 12:
                        print()
                        print(list3)
                        p = input(" Enter name of course : ")
                        while p not in list3:
                            print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                            p = input(" Enter name of course : ")
                        capacity = int(rows[list3.index(p)][3])
                        teacher = rows[list3.index(p)][4]
                        if teacher == 'None':
                            ls = open('course.csv', 'r')
                            reader = csv.reader(ls)
                            myls = list(reader)
                            ls.close()
                            myls[list3.index(p)][4] = self.lname
                            my_new_list = open('course.csv', 'w', newline='')
                            csv_writer = csv.writer(my_new_list)
                            csv_writer.writerows(myls)
                            my_new_list.close()
                            list1.append(p)
                            unit = unit + int(rows[list3.index(p)][1])
                            print(' This unit was successfully selected! ')
                            print()
                        else:
                            print(' Capacity is full! ')
                            print()
                    with open('teacher_course.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow(list1)
            else:
                print()
                logging.warning('a person do select unit as a teacher ! ')
                print(' You have done it befor! ')
                print('-' * 50)
                print()

    def show_3(self):
        list1 = []
        with open("teacher_course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list1.append(i[0])
            try:
                p = list(rows[list1.index(self.use_teacher)])
                print()
                # print('\'your name\'', ', ', '\'courses_1 ...\'', ', ', '\'total units\'')
                print(p)
            except ValueError:
                print()
                print('<<<<<<<<<< Error! First select courses! >>>>>>>>>>')
            print()
            m = input('Enter name of a course or back: ')
            list3 = []
            while m != 'back':
                if m in p:
                    with open("student_course.csv", 'r') as ff:
                        csv_reader = csv.reader(ff)
                        rows = list(csv_reader)
                        for i in rows:
                            if m in i:
                                list3.append(i[0])
                            else:
                                print(' Nobody get this course! ')
                        print(list3)
                else:
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                m = input("Enter back ")
        print('-' * 50)
        print()


