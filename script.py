#!/usr/bin/python3
if __name__ == "__main__":
    import random
    from modules import *



    rows = 0
    listOfValues = []
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
        rows = random.randint(1, 20)
        for i in range(1, rows):
            listOfValues = [
                    randomTitle(),
                    randomDescription(),
                    randomType(),
                    randomPriority(),
                    randomStatus(),
                    randomDuedate(),
                    randomTimes(),
                    randomTimes(),
                    "",
                    randomOS(),
                    randomBrowserName(),
                    randomEstimatedAndLogged(),
                    randomEstimatedAndLogged()
            ]
            
        fd.write("{}\n".format(",".join(listOfValues)))
        listOfValues = []
        
        fd.close()
