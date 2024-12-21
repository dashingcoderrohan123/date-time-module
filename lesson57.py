#Write a program to generate a random date and time from the given start and end dates

import random
import time

def getRandomDate(startdate, enddate):
    print("printing random date between",startdate," and ",enddate)
    randomGenerator=random.random()
    date_format="%m/%d/%Y" 
    start_time=time.mktime(time.strptime(startdate,date_format))   
    end_time=time.mktime(time.strptime(enddate,date_format)) 
    randomtime=start_time+randomGenerator*(end_time-start_time)
    randomdate=time.strftime(date_format,time.localtime(randomtime))
    return randomdate
print("Random date =",getRandomDate("01/01/2020","01/01/2024"))
