import login, register

print()
print("********** WELCOME **********")
print("1. Register \n2. Login to account \n3. Exit")
m = int(input("select number of your choice: "))

if m == 1:
    n = int(input("1. student or 2. education responsible: "))
    if n == 1:
        register.RegisterStudent(n).input1()
    elif n == 2:
        register.RegisterEducationResponsible(n)
    else:
        raise Exception('Error! please run again and enter a current number!')
elif m == 2:
    login.Login()
elif m == 3:
    print('Good Lock')
else:
    # print('Error! please run again and enter a current number')
    raise Exception('Error! please run again and enter a current number!')

