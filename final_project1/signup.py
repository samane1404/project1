import re
import csv
import hashlib
import logging

def student():
    input_1(file_1='student.csv', id=14000114)

def teacher():
    input_1(file_1='teacher.csv', id=14001003)

def education_responsible():
    input_1(file_1='education_responsible.csv', id=14000608)

def input_1(file_1, id):

    while True:
        try:
            fname_student = input('Enter your first name: ')
            if len(fname_student) == 0 or fname_student == ' ':
                raise ValueError('<<<<<<<<<< Error! Try again! >>>>>>>>>>')
            break
        except ValueError as error:
            logging.warning('a person entered invalid first name for registering as a student ! ')
            print(error)
    while True:
        try:
            lname_student = input('Enter your last name: ')
            if len(lname_student) == 0 or lname_student == ' ':
                raise ValueError('<<<<<<<<<< Error! Try again! >>>>>>>>>>')
            break
        except ValueError as error:
            logging.warning('a person entered invalid last name for registering as a student ! ')
            print(error)
    list1 = []
    with open(file_1, 'r') as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
        for i in rows:
            list1.append(i[0])
        while True:
            try:
                use_student = input('Enter a username (Preferably your name): ')
                if use_student in list1 or len(use_student) == 0 or use_student == ' ':
                    raise ValueError('<<<<<<<<<< Error! Try again! >>>>>>>>>>')
                break
            except ValueError as error:
                logging.warning('a person entered invalid username for registering as a student ! ')
                print(error)
    while True:
        try:
            pass_student = input('Enter a password (At least 8 characters including numbers, letters and symbols): ')
            if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%&])[\w\d@#$%&]{6,12}$", pass_student):
                raise ValueError('<<<<<<<<<< Error! not valid >>>>>>>>>>')
            break
        except ValueError as error:
            logging.warning('a person entered the wrong password for registering as a student ! ')
            print(error)
    while True:
        try:
            pass_student_again = input('Enter password again: ')
            if pass_student != pass_student_again:
                raise ValueError('<<<<<<<<<< Error! enter password again! >>>>>>>>>>')
            break
        except ValueError as error:
            logging.warning('a person entered the wrong re_password for registering as a student ! ')
            print(error)
    hashing = pass_student_again.encode()
    with open(file_1, 'a', newline='') as f:
        with open(file_1, 'r') as ff:
            reader = csv.reader(ff, delimiter=",")
            data = list(reader)
            row_count = len(data)
        write = csv.DictWriter(f, fieldnames=['first_name:', 'last_name:', 'username:', 'password:', 'id:', 'sha256:'])
        if f.tell() == 0:
            write.writeheader()
        write.writerows([{'first_name:':fname_student, 'last_name:':lname_student, 'username:': use_student, 'password:': pass_student, 'id:': id + row_count,
                          'sha256:': hashlib.sha256(hashing).hexdigest()}])
    logging.info('One person successfully registered as student! ')
    print()
    print(f'******************************\nPersonal ID is : {id + row_count}\n******************************')
    print()