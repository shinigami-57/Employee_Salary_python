import empdetails as empdt
import updateDetails as updt
import genSalary as sal
import SignUp as sup
from datetime import  date
from datetime import  datetime
count1=0
check=0
global flag
flag=0
print()
print('--- WELCOME TO EMPLOYEE PAYROLL SYSTEM ---')
while count1 == 0 and check == 0:
    try:
        print("1.Sign Up\n2.Login\n3.Change Password\n")
        ch=int(input("Enter your Choice: "))
        if (ch == 1):
            flag=sup.snup()
        elif(ch == 2):
            flag,user=sup.login()

#The main Function as soon as we login

            count2 = 0
            while count2 == 0 and flag == 1:
                print('--- FEATURES ---')
                try:
                    print("1.View Employee Details\n2.Update Details\n3.Generate Salary Report\n4.Logout")
                    ch = int(input("Enter your Choice: "))

                    if (ch == 1):
                        empid = int(input('Enter the Employee ID: '))
                        result = empdt.empfunc(empid)
                        print(result)
                        print('\nEmployee ID:%s\nName:%s\nDepartment:%s\nSalary:%s\n4.Leaves:%s' % (
                        result[0], result[1], result[2], result[3], result[4]))
                        print("_" * 15 + "\n")

                    elif (ch == 2):
                        updt.updtfunc()

                    elif (ch == 3):
                        sal.gensal(user)

                    elif (ch == 4):
                        count2 = 1
                        check=1
                        print("\nLogout Successfull!ThankYou!!!")
                        with open('logs.txt','a') as f:
                            f.write('--LOGOUT--'+"\n"+'By: {0}\nDate: {1}\nTime: {2}\n'.format(user,date.today(),datetime.now().time())+"\n")


                    else:
                        print('Invalid Choice ! ')
                        print("_" * 15 + "\n")

                except Exception:
                    print("\nSelect a Number from the available choices !!!\n")
        elif(ch == 3):
            sup.change()
        elif ch == 4:
            print('ThankYou!')
            count1=1
        else:
           print('Invalid Choice ! ')
           print("_" * 15 + "\n")

    except Exception:
     print("\nSelect a Number from the available choices !!!\n")





