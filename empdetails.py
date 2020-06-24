import ast
f = open('data.txt', 'r+')
contents = f.read()
emp_details = ast.literal_eval(contents)
f.close()


def empfunc(empid):

    empName=emp_details[empid][0]
    empDept=emp_details[empid][1]
    empSal=emp_details[empid][2]
    empLeaves = emp_details[empid][3]
    return empid,empName,empDept,empSal,empLeaves