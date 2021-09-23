
class RegisterStudent:
    def __init__(self, n):
        self.n = n
        self.use_student = None
        self.pass_student = None
        self.pass_student_again = None

    def input1(self):
        self.use_student = input("Enter a username: ")
        if self.use_student == '':
            raise Exception('This field should\'nt be empty')
        self.pass_student = input("Enter a password (At least 8 characters including numbers, letters and symbols): ")
        if self.pass_student == '':
            raise Exception('This field should\'nt be empty')
        self.pass_student_again = input("Enter a password again: ")


class RegisterEducationResponsible:
    def __init__(self, n):
        self.n = n
        print(self.n)