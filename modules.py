#!/usr/bin/python3
import random
import requests


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
