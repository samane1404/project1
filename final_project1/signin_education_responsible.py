import csv
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class EducationResponsible:
    def __init__(self):
        self.use_responsible = None
        self.pas_responsible = None
        self.fname = None
        self.lname = None

    def login(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        with open('education_responsible.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list1.append(row['username:'])
                list2.append(row['password:'])
                list3.append(row['first_name:'])
                list4.append(row['last_name:'])
        self.use_responsible = input('Enter username: ')
        while True:
            try:
                if self.use_responsible not in list1:
                    raise ValueError('<<<<<<<<<< Error! enter correct username! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong username for logging in as a education_responsible ! ')
                print(error)
                self.use_responsible = input('Enter username: ')
        self.pas_responsible = input('Enter password: ')
        while True:
            try:
                if self.pas_responsible not in list2:
                    raise ValueError('<<<<<<<<<< Error! enter correct password! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for logging in as a education_responsible ! ')
                print(error)
                self.pas_responsible = input('Enter password: ')
        self.fname = list3[list1.index(self.use_responsible)]
        self.lname = list4[list1.index(self.use_responsible)]
        EducationResponsible.menu(self)

    def menu(self):
        logging.info('One person successfully log in as education responsible! ')
        while True:
            try:
                print()
                print(f'******************** Hi {self.fname} {self.lname} ********************')
                k = int(input(
                    '1. show list of courses \n2. search course by name \n3. show total units \n4. define a new course'
                    '\n5. show list of student  \n6. search student by name or id \n7. select a course and show list of student'
                    '\n8. select a student and show list of courses \n9. reject/approve a selected courses by students \n10. back'
                    '\nselect number of your choice: '))
                break
            except ValueError:
                print()
                print('<<<<<<<<<< Error! this is not number! >>>>>>>>>>')
                continue
        while k != 10:
            if k == 1:
                EducationResponsible.show_1(self)
            elif k == 2:
                EducationResponsible.search_1(self)
            elif k == 3:
                EducationResponsible.show_2(self)
            elif k == 4:
                EducationResponsible.define_1(self)
            elif k == 5:
                EducationResponsible.show_3(self)
            elif k == 6:
                EducationResponsible.search_2(self)
            elif k == 7:
                EducationResponsible.select_1(self)
            elif k == 8:
                EducationResponsible.select_2(self)
            elif k == 9:
                EducationResponsible.reject_approve(self)
            else:
                print('\n<<<<<<<<<< Error! this number is not correct! >>>>>>>>>>')
            while True:
                try:
                    print()
                    print(f'******************** Hi {self.fname} {self.lname} ********************')
                    k = int(input(
                        '1. show list of courses \n2. search course by name \n3. show total units \n4. define a new course'
                        '\n5. show list of student  \n6. search student by name or id \n7. select a course and show list of student'
                        '\n8. select a student and show list of courses \n9. reject/approve a selected courses by students \n10. back'
                        '\nselect number of your choice: '))
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
        df2 = pd.read_csv('course.csv')
        df2['units:'].sum()
        print('-' * 50)
        print('total units = ' , df2['units:'].sum())
        print('-' * 50)
        print()

    def define_1(self):
        print()
        les = input("Enter name of new course: ")
        list4 = []
        with open('course.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                list4.append(row['lesson:'])
        while True:
            try:
                if les in list4:
                    raise ValueError('<<<<<<<<<< Error! this course exist! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.info('education responsible entered duplicate course! ')
                print(error)
                les = input("Enter another course: ")
        uni = input("units: ")
        cap = input("capacity: ")
        r_cap = input("remain_capacity: ")
        teach = input("teacher: ")
        with open('course.csv', 'a', newline='') as f:
            write = csv.DictWriter(f, fieldnames=['lesson:', 'units:', 'capacity:', 'remain_capacity:', 'teacher:'])
            if f.tell() == 0:
                write.writeheader()
            write.writerows(
                [{'lesson:': les, 'units:': uni, 'capacity:': cap, 'remain_capacity:': r_cap, 'teacher:': teach}])
            logging.info('education responsible entered new course! ')
        print('-' * 50)
        print()

    def show_3(self):
        list3 = []
        with open("student.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list3.append(i[1])
            print(list3)
            print('-' * 50)
            print()
    def search_2(self):
        list2 = []
        list3 = []
        with open("student.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list2.append(i[1])
                list3.append(i[4])
            print()
            p = input("Enter last name of student or student ID : ")
            while p != 'back':
                if p in list3:
                    with open("student.csv", 'r') as f:
                        csv_reader = csv.reader(f)
                        rows = list(csv_reader)
                        for i in rows:
                            if p in i:
                                y = i[2]
                                with open("student_course.csv", 'r') as h:
                                    csv_readerr = csv.reader(h)
                                    rowss = list(csv_readerr)
                                    for r in rowss:
                                        if y in r:
                                            print()
                                            print(r)
                            # else:
                            #     print(' This student select any course! ')
                elif p in list2:
                    with open("student_course.csv", 'r') as f:
                        csv_reader = csv.reader(f)
                        rows = list(csv_reader)
                        for i in rows:
                            if p in i:
                                print()
                                print(i)
                            # else:
                            #     print(' This student select any course! ')
                else:
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                p = input("Enter name of student or student number or back : ")
            print('-' * 50)
            print()

    def select_1(self):
        list1 = []
        with open("course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list1.append(i[0])
            print()
            print(list1)
            m = input(' Enter name of a course or back: ')
            list3 = []
            while m != 'back':
                if m in list1:
                    with open("student_course.csv", 'r') as ff:
                        csv_reader = csv.reader(ff)
                        rows = list(csv_reader)
                        for i in rows:
                            if m in i:
                                list3.append(i[0])
                            # else:
                            #     print(' Nobody get this course! ')
                        print(list3)
                else:
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                print()
                m = input(" Enter back: ")
        print('-' * 50)
        print()

    def select_2(self):
        list1 = []
        with open("student_course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list1.append(i[0])
            print()
            print(list1)
            m = input('Enter name of a student or back: ')
            list3 = []
            while m != 'back':
                if m in list1:
                    with open("student_course.csv", 'r') as ff:
                        csv_reader = csv.reader(ff)
                        rows = list(csv_reader)
                        for i in rows:
                            if m in i:
                                print(i)
                                # list3.append(i[0])
                            # else:
                            #     print(' This student get any course! ')

                else:
                    print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
                m = input("Enter back ")
        print('-' * 50)
        print()

    def reject_approve(self):
        list3 = []
        with open("student_course.csv", 'r') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
            for i in rows:
                list3.append(i[0])
            print()
            print('List of student do select units: ')
            print(list3)
            p = input("do you approve?(Y/N) : ")
            if p == 'Y':
                print()
                print(' That\s Good! ')
            elif p == 'N':
                m = input('which? ')
                if m in list3:
                    s = list(rows[list3.index(m)])
                    print(s)
                    k = str(input(' which course? or back? '))
                    ls = open('student_course.csv', 'r')
                    reader = csv.reader(ls)
                    myls = list(reader)
                    ls.close()
                    myls[list3.index(m)][s.index(k)] = '-'
                    my_new_list = open('student_course.csv', 'w', newline='')
                    csv_writer = csv.writer(my_new_list)
                    csv_writer.writerows(myls)
                    my_new_list.close()
                    list9 = []
                    with open("course.csv", 'r') as y:
                        csv_reader = csv.reader(y)
                        rows1 = list(csv_reader)
                        for i in rows1:
                            list9.append(i[0])
                        ls1 = open('course.csv', 'r')
                        reader1 = csv.reader(ls1)
                        myls1 = list(reader1)
                        ls1.close()
                        myls1[list9.index(k)][3] = int(rows1[list9.index(k)][3])+1
                        my_new_list = open('course.csv', 'w', newline='')
                        csv_writer = csv.writer(my_new_list)
                        csv_writer.writerows(myls1)
                        my_new_list.close()
                    print()
                    print('it Done!')
            else:
                print('\n<<<<<<<<<< Error! this word is not correct! >>>>>>>>>>')
        print('-' * 50)
        logging.warning(' result of select unit approve by education_responsible ! ')
        print()




