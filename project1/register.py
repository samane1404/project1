import re
import csv
import hashlib
import logging

logging.basicConfig(level=logging.DEBUG, filename='loging.log', format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class RegisterStudent:
    def __init__(self, n):
        self.n = n
        self.id = 14000114
        self.use_student = None
        self.pass_student = None
        self.pass_student_again = None

    def input1(self):
        while True:
            try:
                self.use_student = input("Enter a username: ")
                if len(self.use_student) == 0 or self.use_student == ' ':
                    raise ValueError('((((((((((Error! this field should not be empty!))))))))))')
                logging.warning('a person entered nothing username for registering as a student ! ')
                break
            except ValueError as error:
                print(error)
        while True:
            try:
                self.pass_student = input("Enter a password (At least 8 characters including numbers, letters and symbols): ")
                if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%&])[\w\d@#$%&]{6,12}$", self.pass_student):
                    raise ValueError('((((((((((Error! not valid))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered the wrong password for registering as a student ! ')
                print(error)
        while True:
            try:
                self.pass_student_again = input("Enter password again: ")
                if self.pass_student != self.pass_student_again:
                    raise ValueError('((((((((((Error! enter password again!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered the wrong re_password for registering as a student ! ')
                print(error)
        hashing = self.pass_student_again.encode()
        with open('text.csv', 'a', newline='') as f:
            with open('text.csv', "r") as ff:
                reader = csv.reader(ff, delimiter=",")
                data = list(reader)
                row_count = len(data)
            write = csv.DictWriter(f, fieldnames=['username:', 'password:', 'id:', 'sha256:'])
            if f.tell() == 0:
                write.writeheader()
            write.writerows([{'username:': self.use_student, 'password:': self.pass_student, 'id:': self.id+row_count,
                              'sha256:': hashlib.sha256(hashing).hexdigest()}])
        logging.info('One person successfully registered as student! ')
        print()
        print(f'******************************\nstudent number is : {self.id+row_count}\n******************************')
        print()

class RegisterEducationResponsible:
    def __init__(self, n):
        self.n = n
        self.use_responsible = None
        self.pass_responsible = None
        self.pass_responsible_again = None

    def input2(self):
        while True:
            try:
                self.use_responsible = input("Enter a username: ")
                if len(self.use_responsible) == 0 or self.use_responsible == ' ':
                    raise ValueError('((((((((((Error! this field should not be empty!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered nothing username for registering as a education responsible ! ')
                print(error)
        while True:
            try:
                self.pass_responsible = input("Enter a password (At least 8 characters including numbers, letters and symbols): ")
                if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", self.pass_responsible):
                    raise ValueError('((((((((((Error! not valid))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong password for registering as a education responsible ! ')
                print(error)
        while True:
            try:
                self.pass_responsible_again = input("Enter password again: ")
                if self.pass_responsible != self.pass_responsible_again:
                    raise ValueError('((((((((((Error! enter password again!))))))))))')
                break
            except ValueError as error:
                logging.warning('a person entered wrong re_password for registering as a education responsible ! ')
                print(error)
        hashing = self.pass_responsible.encode()
        with open('textt.csv', 'a', newline='') as f:
            write = csv.DictWriter(f, fieldnames=['username:', 'password:', 'sha256:'])
            if f.tell() == 0:
                write.writeheader()
            write.writerows([{'username:': self.use_responsible, 'password:': self.pass_responsible, 'sha256:': hashlib.sha256(hashing).hexdigest()}])
        logging.info('One person successfully registered as education responsible! ')
        print()
        print(f'******************************GOOD LUCK******************************')
        print()
