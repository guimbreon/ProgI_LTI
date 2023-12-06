import infoFromFiles
import infoToFiles
from constants import *
#FILES
#DOCTORS
fileNameDoctors = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/doctors14h00.txt"
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet4/doctors18h00.txt"
#REQUESTS
fileNameRequests = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/requests14h30.txt"
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet1/requests10h30.txt"
#SCHEDULE
fileNameSchedule = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/schedule14h00.txt"

#TO REDIRECT TO ANOTHER HOSPITAL
#fileNameDoctors = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/doctors16h00.txt"
#fileNameRequests = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/requests16h30.txt"
#fileNameSchedule = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/schedule16h00.txt"



#TESTING
doctorsData,doctorsInfo = infoFromFiles.readDoctorsFile(fileNameDoctors)
requestsData, requestsInfo = infoFromFiles.readRequestsFile(fileNameRequests)
scheduleData,scheduleInfo = infoFromFiles.readScheduleFile(fileNameSchedule)
#infoFromFIles
#print(doctorsData)
print(requestsData)
#print(scheduleData)

"""

list = [["a",7],["b",12],["d",5],["c",4],["k",12],["d",12]]

print(sorted(list,key=lambda x: (x[1],x[0])))
"""
"""
my_list = [['Guilherme Gaspar', '2', [14, 20], '40', [39, 50]],
           ['Horácio Horta', '3', [15, 20], '120', [7, 20]],
           ['Ildefonso Inácio', '2', [15, 27], '40', [39, 50]],
           ['José Justo', '2', [9, 20], '40', [15, 0]]]

# Sort the list based on the third element and then the second element of each sublist
sorted_list = sorted(my_list, key=lambda x: (int(x[DOCT_TIME_IDK][0]),int(x[DOCT_TIME_IDK][1]), -int(x[DOCT_CAT_IDX]),int(x[DOCT_MINS_IDX]) , int(x[DOCT_TOTALTIME_IDX][0]), int(x[DOCT_TOTALTIME_IDX][1]), x[DOCT_NAME_IDX]))

print(sorted_list)
"""
"""
import copy
from constants import *
myList = [['Joana Joanes', '22', 'red', 'medium'], 
          ['Graça Gonçalves', '22', 'green', 'low'], 
          ['Irene Ilídio', '22', 'yellow', 'high'], 
          ['Hortênsia Holmes', '27', 'yellow', 'low'],
          ['Batata gira','22',"yellow","high"]]
newList = []
for item in myList:
    print(item)
    if item[MOTH_WRIST_IDK] == "green":
        item[MOTH_WRIST_IDK] = 1
    elif item[MOTH_WRIST_IDK] == "yellow":
        item[MOTH_WRIST_IDK] = 2
    else:
        item[MOTH_WRIST_IDK] = 3

    if item[MOTH_IMP_IDK] == "low":
        item[MOTH_IMP_IDK] = 1
    elif item[MOTH_IMP_IDK] == "medium":
        item[MOTH_IMP_IDK] = 2
    else:
        item[MOTH_IMP_IDK] = 3
    newList.append(item)

sortedList = sorted(newList,key=lambda x: (-int(x[MOTH_IMP_IDK]),-int(x[MOTH_WRIST_IDK]),-int(x[MOTH_AGE_IDK]),x[MOTH_NAME_IDX]))
print(sortedList)
"""



"""
TRYING TO DO PLANNNING
"""
import planning

import dateTime
doctorsData #dados medico
requestsData #dados maes
scheduleData #dados antigos
print("original",doctorsData)
#print(requestsData)

timeSchedule = [dateTime.hourToInt(scheduleInfo[1][3].rstrip()),dateTime.minutesToInt(scheduleInfo[1][3].rstrip())]


planningRequest,plannningDoctors = planning.updateSchedule(doctorsData,requestsData,scheduleData,
	dateTime.add30Min(timeSchedule))

print(planningRequest)

"""

import dateTime
medico = ["gui","3",[14,40],'220',[39,20]]
print(dateTime.add20Min(medico))
"""

"""
TRYING TO DO infoToFiles
"""
header = infoToFiles.headerWork(doctorsInfo[1])
sched = ["i","dont","have","it"]
fileOutputFile = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/poh"
#infoToFiles.writeScheduleFile(planningRequest, header, fileOutputFile)
infoToFiles.writeDoctorsFile(plannningDoctors, header, fileOutputFile)

