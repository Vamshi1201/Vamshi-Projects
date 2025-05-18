def printperson(data):
    for k, v in data.items():
        print(k, ':', v)

#mydata = {'name':'vamshi', 'age':24, 'city':'korutla','country':'india'}
#printperson(mydata)

userdata = {}
e = 1
while e != '0':
    userkey = input("enter key : ")
    uservalue = input ("enter value : ")
    userdata[userkey] = uservalue

    printperson(userdata)
    input()


