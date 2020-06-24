from empdetails import *
from datetime import date
import Transaction as trans
def gensal(user):
    finalsal=0
    today = date.today()
    emp_id = int(input('Enter the Employee ID: '))
    if (emp_details[emp_id][2] > 10000) and (emp_details[emp_id][2] <= 20000):
        taxn = '15%'
        tax = (0.15 * (emp_details[emp_id][2] - 10000))
        sal = emp_details[emp_id][2] - tax

    elif (emp_details[emp_id][2] > 20000) and (emp_details[emp_id][2] <= 35000):
        taxn = '20%'
        tax = (0.2 * (emp_details[emp_id][2] - 20000))
        sal = emp_details[emp_id][2] - tax

    elif (emp_details[emp_id][2] > 35000) and (emp_details[emp_id][2] <= 50000):
        taxn = '25%'
        tax = (0.25 * (emp_details[emp_id][2] - 35000))
        sal = emp_details[emp_id][2] - tax

    elif (emp_details[emp_id][2] > 50000):
        taxn = '30%'
        tax = (0.3 * (emp_details[emp_id][2] - 50000))
        sal = emp_details[emp_id][2] - tax

    def leave():
        nonlocal sal

        #print("The total leaves taken by the Employee:%s\n" % (emp_details[emp_id][3]))

        if (emp_details[emp_id][3] > 15) and (emp_details[emp_id][3] <= 25):
            count = abs(15 - (emp_details[emp_id][3]))
            sal_leave = (sal - (count * 500))

        elif (emp_details[emp_id][3] > 25) and (emp_details[emp_id][3] <= 30):
            count = abs(25 - (emp_details[emp_id][3])) + 10
            sal_leave = (sal - (count * 500))

        elif (emp_details[emp_id][3] > 30) and (emp_details[emp_id][3] <= 45):
            count = abs(30 - (emp_details[emp_id][3])) + 20
            sal_leave = (sal - (count * 500))

        elif (emp_details[emp_id][3] > 45):
            sal_leave = sal - 15000

        else:
            sal_leave = sal
        print('--- SALARY REPORT ---')
        print('Name: %s\nDepartment: %s\nGross salary: %s\nTax: %s\nNet Salary: %s\nDate: %s'
              % (emp_details[emp_id][0], emp_details[emp_id][1], emp_details[emp_id][2], taxn, sal_leave, today.strftime("%B %d, %Y")))
        print("_" * 15 + "\n")
        return sal_leave
    finalsal=leave()
    print('Initiate Transaction\n1:YES\n2:NO\n')
    ch = int(input('Enter your choice: '))
    if (ch == 1):
        trans.trans(user,emp_id,finalsal)
    elif (ch == 2):
        print('TRANSACTION NOT INITIATED')
