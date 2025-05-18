def person(**data):
    # print(data)
    for k, v in data.items():
        if k == 'firstname':
           print(k, ' :', v)
        elif k == 'lastname':
           print(k, '  :', v)
        elif k == 'age':
           print(k, '       :', v)
        else:
           print(k, '  :', v)
fname = input ("enter your first name: ")
lname = input ("enter your last name: ")
age = input ("enter your age: ")
mobile = input ("enter your mobile no: ")
person(firstname=fname, lastname=lname, age=age, mobileno=mobile)
input()