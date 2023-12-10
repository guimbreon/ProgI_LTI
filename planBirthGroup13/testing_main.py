import refresh
import planning
import infoFromFiles
import dateTime
#FILES
#DOCTORS
fileNameDoctors = "/home/guimbreon/Desktop/Trabalho/testSets_v5/testSet1/doctors10h00.txt"
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet4/doctors18h00.txt"
#REQUESTS
fileNameRequests = "/home/guimbreon/Desktop/Trabalho/testSets_v5/testSet1/requests10h30.txt"
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet1/requests10h30.txt"
#SCHEDULE
fileNameSchedule = "/home/guimbreon/Desktop/Trabalho/testSets_v5/testSet1/schedule10h00.txt"

#TO REDIRECT TO ANOTHER HOSPITAL
#fileNameDoctors = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/doctors16h00.txt"
#fileNameRequests = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/requests16h30.txt"
#fileNameSchedule = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet3/schedule16h00.txt"
#refresh.plan(fileNameDoctors,fileNameSchedule,fileNameRequests)
doctorsData, doctorsInfo = infoFromFiles.readDoctorsFile(fileNameDoctors)
requestsData, requestsInfo = infoFromFiles.readRequestsFile(fileNameRequests)
scheduleData, scheduleInfo = infoFromFiles.readScheduleFile(fileNameSchedule)

timeSchedule = [dateTime.hourToInt(scheduleInfo[1][3].rstrip()),dateTime.minutesToInt(scheduleInfo[1][3].rstrip())]
timeSchedule = dateTime.add30Min(timeSchedule)
newRequests, newDoctors = planning.updateSchedule(doctorsData, requestsData, scheduleData, timeSchedule)

print(newDoctors)

print(newRequests)