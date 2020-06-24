from datetime import date
from datetime import datetime
def trans(user,id,sal):
    print('TRANSACTION INITIATED')
    with open('logs.txt', 'a') as f:
        f.write('--TRANSACTION INITIATED--'+'\n'+'By: {0}\nFor Employee: {1}\nAmount: {2}\nDate: {3}\nTime: {4}\n'.format(user, id,sal,date.today(), datetime.now().time()) + "\n")

