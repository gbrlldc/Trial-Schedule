import schedule
import time

#set up
def job1():
    print("Hello world in minutes!")

def job2():
    print("Hello world in hours!")

#Ask if user would like to schedule every() minute or every hours 
#note - this is case sensitive
input1 = input ('minutes or hours? ')

#If minutes; 
if input1 == 'minutes':
    Minutes = int(input("Number in minutes:"))
    schedule.every(Minutes).minutes.do(job1)

#if hours;
elif input1 == 'hours':
    Hours = int(input("Number in hours:"))
    schedule.every(Hours).hours.do(job2)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
