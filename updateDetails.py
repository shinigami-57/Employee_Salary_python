from empdetails import *


def updtfunc():
    emp_id=int(input('Enter the Employee ID: '))
    print("1.Name\n2.Department\n3.Salary\n4.Leaves")
    ch=int(input('Choose the field you want to update: '))
    print("_" * 15 + "\n")

    if(ch == 1):
        n=input('Enter the New Name: ')
        emp_details[emp_id][0]=n
        result=empfunc(emp_id)

        f = open("data.txt", "w")
        f.write(str(emp_details))
        f.close()
        print("_" * 15 + "\n")
        print('Employee ID:%s\nName:%s\nDepartment:%s\nSalary:%s\nLeaves%s'% (result[0], result[1], result[2], result[3], result[4]))
        print("_" * 15 + "\n")


    elif (ch == 2):
        n = input('Enter the New Department: ')
        emp_details[emp_id][1] = n
        result = empfunc(emp_id)

        f = open("data.txt", "w")
        f.write(str(emp_details))
        f.close()
        print("_" * 15 + "\n")
        print('Employee ID:%s\nName:%s\nDepartment:%s\nSalary:%s\nLeaves%s' % (result[0], result[1], result[2], result[3], result[4]))
        print("_" * 15 + "\n")


    elif (ch == 3):
        n = int(input('Enter the New Salary: '))
        emp_details[emp_id][2] = n
        result = empfunc(emp_id)

        f = open("data.txt", "w")
        f.write(str(emp_details))
        f.close()
        print("_" * 15 + "\n")
        print('Employee ID:%s\nName:%s\nDepartment:%s\nSalary:%s\n4.Leaves%s' % (result[0], result[1], result[2], result[3], result[4]))
        print("_" * 15 + "\n")

    elif (ch == 4):
        n = int(input('Enter the New Leaves number: '))
        emp_details[emp_id][3] = n
        result = empfunc(emp_id)

        f = open("data.txt", "w")
        f.write(str(emp_details))
        f.close()
        print("_" * 15 + "\n")
        print('Employee ID:%s\nName:%s\nDepartment:%s\nSalary:%s\n4.Leaves:%s' % (result[0], result[1], result[2], result[3], result[4]))
        print("_" * 15 + "\n")

    else:
        print('Invalid Choice!')