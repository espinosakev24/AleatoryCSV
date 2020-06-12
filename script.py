#!/usr/bin/python3
import random
import modules

numberFiles = 10
columnTitles = [
    "Title",
    "Description",
    "Type",
    "Priority",
    "Status",
    "DueDate",
    "Created",
    "Updated",
    "Resolution",
    "OS",
    "BrowserName",
    "LoggedTime",
    "EstimatedTime",
]
for n in range(0, numberFiles):
    fd = open("fileForTest_{}.csv".format(n), "w")
    fd.write("{}\n".format(",".join(columnTitles)))
    fd.write("this value should be below the tiltes row")

#    for i in range(0, random.randint(5, 10):

        
    fd.close()

