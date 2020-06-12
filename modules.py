#!/usr/bin/python3
import random
import requests
import datetime


def randomTitle():
    jsonArr = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    randomIdx = random.randint(0, 20)
    randTitle = jsonArr[randomIdx]["title"]
    return randTitle

def randomDescription():
    jsonArr = requests.get("https://jsonplaceholder.typicode.com/comments").json()
    randomIdx = random.randint(0, 20)
    randomDescription = jsonArr[randomIdx]["body"]
    return randomDescription

def randomPriority():
    prioritiesList = [
        "Open", "Waiting on Client", "In Progress",
        "Defer", "Resolved/Fixed", "QA Verified", "",
        "Won’t Fix", "Duplicate", "User Error", "Reopen",
        "QA Verify"
    ]
    return prioritiesList[random.randint(0, len(prioritiesList) - 1)]

def randomType():
    typeList = [
        "Bug", "Enhancement", "Feature", "Task", "",
    ]
    return typeList[random.randint(0, len(typeList) - 1)]
print(randomType())

def randomOS():
    oslist = ["Windows 10", "MAC", "Linux", "Ubuntu"]
    return oslist[random.randint(0, len(oslist) - 1)]

def randomBrowserName():
    browserlist = ["Opera", "Chrome 1.2", "Firefox 3.4.2", "Explorer 8"]

def randomDuedate():
    start_date = datetime.date(2016, 1, 1)
    end_date = datetime.date(2021, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%m/%d/%Y")

def randomEstimatedAndLogged():
    hours = random.randint(0, 24)
    minutes = random.randint(0, 59)
    timeFormat = datetime.time(hours, minutes)
    return (timeFormat.strftime("%H:%M"))

