import login, register
m = input('hello')
if m == 't':
    login.Login('3')
elif m == 'p':
    register.Register('5')
else:
    print('bye, bye')
