#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62371 Duarte Soares
import infoFromFiles
import infoToFiles
import dateTime
import planning
import copy
import sys
"""
COLOCAR AQUI O ARGV E ASSIM

TEMOS Q COLOCAR NO FIM DO FICHEIRO TIPO
updateSchedule(argv[1],argv[2]) OU SEJA LÁ CM É UK
"""

def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested at date d and time t+30mins;
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    doctorsData, doctorsInfo = infoFromFiles.readDoctorsFile(doctorsFileName)
    requestsData, requestsInfo = infoFromFiles.readRequestsFile(requestsFileName)
    scheduleData, scheduleInfo = infoFromFiles.readScheduleFile(scheduleFileName)

    timeSchedule = [dateTime.hourToInt(scheduleInfo[1][3].rstrip()),dateTime.minutesToInt(scheduleInfo[1][3].rstrip())]
    nextSchedTime = dateTime.add30Min(copy.deepcopy(timeSchedule))
    newRequests, newDoctors = planning.updateSchedule(doctorsData, requestsData, scheduleData, nextSchedTime)
    
    timeDoctor = [dateTime.hourToInt(doctorsInfo[1][3].rstrip()),dateTime.minutesToInt(doctorsInfo[1][3].rstrip())]
    nextDoctTime = dateTime.add30Min(copy.deepcopy(timeDoctor))

    headerDoct = infoToFiles.headerWork(doctorsInfo[1])
    doctorsFileName = doctorsFileName.replace(f"doctors{doctorsInfo[1][3].rstrip()}.txt","")
    infoToFiles.writeDoctorsFile(newDoctors, headerDoct, f"{doctorsFileName}doctors{dateTime.intToTime(nextDoctTime[0],nextDoctTime[1])}.txt")

    headerSched = infoToFiles.headerWork(requestsInfo[1])
    scheduleFileName = scheduleFileName.replace(f"schedule{scheduleInfo[1][3].rstrip()}.txt","")
    infoToFiles.writeScheduleFile(newRequests, headerSched, f"{scheduleFileName}schedule{dateTime.intToTime(nextSchedTime[0],nextSchedTime[1])}.txt")

plan(sys.argv[1],sys.argv[2],sys.argv[3])
