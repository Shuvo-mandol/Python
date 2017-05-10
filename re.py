#!/usr/bin/env python3

import datetime
now = datetime.datetime.now()

print('1. Add task :')
print('2. Check task :')
print ('-------------')



def addData():                                                  #Function for adding task

    my_file = open('taskRecord.txt', 'a')
    print('-------------')
    print('Revise after days : ', end='')

    n = int(input())

    day = now.day
    month = now.month
    year = now.year

    counter = 0

    while(counter<=n):

        if month == 2:
            while (1):

                counter = counter + 1
                if day == 28:
                    day = 1
                    month = month + 1
                    break
                else:
                    day = day + 1
                    if counter > n:
                        break

        elif month == 4 or month == 6 or month == 9 or month == 11:
            while (1):

                counter = counter + 1
                if day == 30:
                    day = 1
                    month = month + 1
                    break
                else:
                    day = day + 1
                    if counter > n:
                        break

        else:
            while (1):

                counter = counter + 1
                if day == 31:
                    day = 1
                    month = month + 1
                    if month == 13:
                        month = 1
                        year = year + 1;                      
                        break
                    else:                      
                        break
                else:
                    day = day + 1                    
                    if counter > n:
                        break


    sheduled_day = str(day)
    sheduled_month = str(month)
    sheduled_year = str(year)

    sheduled_date = ""
    sheduled_date += sheduled_day
    sheduled_date += "-"
    sheduled_date += sheduled_month
    sheduled_date += "-"
    sheduled_date += sheduled_year                           #Scheduled date
    sheduled_date += " : "

    print('Add task here : ', end='')
    task = input()
    my_file.write(sheduled_date)
    my_file.write(task)
    my_file.write('\n')
    print('\n','Data saved...')
    my_file.close()




def checkData():                                              #Function to display task

    now = datetime.datetime.now()
    today_date = ""
    day = now.day
    month = now.month
    year = now.year
    today_date += str(day)
    today_date += "-"
    today_date += str(month)
    today_date += "-"
    today_date += str(year)
    today_date += " : "                                       #Todays's date

    print('-------------------------------------','\n')

    serial_of_task = 0
    task_finding_flag = 1

    with open('taskRecord.txt') as my_file:

        for eachLine in my_file:                             #Open file and find task for each line
            finalTask = ""

            if today_date in eachLine:
                serial_of_task = serial_of_task + 1
                for i in range(len(today_date), len(eachLine)):
                        finalTask += eachLine[i]

            if len(finalTask) > 0:
                print(serial_of_task, end='')
                print('.'+'  '+finalTask)                           #Serially print task
                task_finding_flag = 0

        if task_finding_flag == 1:
        	print("Nothing scheduled today....")


try:                                                                #Program starts here

    print('Option : ', end = "")
    userInput = int(input())                                        #Input user option          
    print('-------------')
    if userInput == 1:
        addData()
    elif userInput == 2:
        checkData()
    else:
        print('Invalid input..')
    print('-------------------------------------')

except ValueError:
    print('Invalid input..')
