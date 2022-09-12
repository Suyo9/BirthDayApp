import pandas as pd

from datetime import datetime

import time

import smtplib



def welcome():
    print('\n Walcome to Birthday wishing App \n')
    print(' Choose your option-')
    print('  1. How this works')
    print('  2. create dataset')
    print('  3. use it on existung dataset')
    print("     dataset should be .csv file having clumns 'Name','DOB',MO','Email'")
    


def instructions():
    print('\n** INSTRUCTIONS **')
    print('1. first create dataset(enter option 2),')
    print('2. enter how many records you want to save')
    print('3. enter the details in right format')
    print(' eg. date shouldbe in YYYY-MM-DD format')
    print('\n now press enter to start using (create dataset..)\n')
    nothing = input('')
    


def getData():
    
    dataset2 = [['Name','DOB','MO','Email']]
    
    print('creating Dataset..')
    print("this will overwrite 'dataset.csv' file if present in this directory..")

    no = int(input("\n how may records: "))


    for i in range(no):
        print(f'\nEnter details of #{i+1}')
        data = ['name','dob','mo','email']
        data[0] = input('Name: ')
        str_dob = str(input('DOB YYYY-MM-DD: '))
        dob = datetime.strptime(str_dob,'%Y-%m-%d')
        data[1] = dob.date()
        data[2] = input('Mo: ')
        data[3] = input('Email: ')
        dataset2.append(data)
        
    table = pd.DataFrame(dataset2)

    table.to_csv("dataset.csv",header=False,index=False)
    
    print('Dataset created..')

    time.sleep(3)


def sendmail(name,to):  
    print(f"sending msg to {name}..")
    GMAIL_ID = 'suyoglate555@gmail.com'
    GMAIL_PWD = 'kqwdcdqdxxhzhvru'

    msg = f'Dear {name},\n\nWish you a very happy birthday..! \n\n\t\t\t\t\t-Suyog'

    sub = 'Birthday Greetings!'

    gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)

    gmail_obj.starttls()

    gmail_obj.login(GMAIL_ID, GMAIL_PWD)

    gmail_obj.sendmail(GMAIL_ID, to,f"Subject : {sub}\n\n{msg}")

    gmail_obj.quit()

    print(f'\nBday greetings sent to {name}')


# read csv

def readData():
    print("\nReading data from 'dataset.csv'..\n")
    table3 = pd.read_csv("dataset.csv")

    date = datetime.today()

    found = False
    
    bdayList = []

    for k in table3['DOB']:

        bday = datetime.strptime(k,"%Y-%m-%d")
        tday = date.today()
        if bday.day == tday.day and bday.month == tday.month:
            found = True
            
            name = table3[table3['DOB']==k]['Name'].item()
            mob = table3[table3['DOB']==k]['MO'].item()
            email = table3[table3['DOB']==k]['Email'].item()
            
            print(f"\nIt's {name}'s Birthday! \n")
            msg = input('press enter to send greetings press 1 to skip:')
            if msg=='1':
                print(f'\n{name} skiped')
                continue
            else:
                sendmail(name,email)
    print('\nAll done.')
        
    if not found:
        print('no birthday today')
    input('')


welcome()

choice = int(input("\n Choice: "))



if choice == 1:
    instructions()
    getData()
    readData()
elif choice == 2:
    getData()
    readData()
elif choice == 3:
    readData()
else :
    welcome()
