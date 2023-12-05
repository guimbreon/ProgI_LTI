#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62371 Duarte Soares


"""
Nas funções readDoctorsFile, readRequestsFile e readScheduleFile, todas fazem o mesmo
então poderiamos substituir pela função readFile?
NÃO POIS TEMOS QUE LEVANTAR O ERROR(PAGINA) DA PAGINA 9.
"""
from constants import *
import dateTime
def readFile(fileName):
    """
    Reads a given file from fileName and turn it into a collection and it's type(Requests,Doctors or Schedule).

    Requires:
    fileName is a str with the path of the .txt file organized as in the examples provided 
    in the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to the Data from each line in the file located at fileName
    fileInfo which represents the type of file it's reading.
    """
    fileData = open(fileName, "r")
    newList = []
    fileInfo = []
    header = []
    lineNum = 0
    for line in fileData:
        if lineNum <= 6:
            header.append(line)
        if lineNum == 6:
            fileInfo.append(line.rstrip())
        if lineNum > 6 and len(line.split()) != 0:
            newLine = line.rstrip().split(", ")
            finalLine = []
            for item in newLine:
                if "h" in item and item[0].isdigit(): #it separates hours and minutes into a list
                    timeList =[]
                    timeList.append(dateTime.hourToInt(item))
                    timeList.append(dateTime.minutesToInt(item))
                    finalLine.append(timeList)
                else:
                    finalLine.append(item)
            newList.append(finalLine)
        lineNum += 1
    fileData.close()
    fileInfo.append(header)
    return newList, fileInfo
    
def sortDoctor(doctors):
    """
    Sort a doctors given list.

    Requires:
    - doctors (lst)(lst) : contains a list of lists where each list  corresponds to a doctor.
    Ensures:
    New doctors list but now is sorted the given arguments.
    """
    return sorted(doctors, key=lambda x: (int(x[DOCT_TIME_IDK][0]),int(x[DOCT_TIME_IDK][1]), -int(x[DOCT_CAT_IDX]),int(x[DOCT_MINS_IDX]) , int(x[DOCT_TOTALTIME_IDX][0]), int(x[DOCT_TOTALTIME_IDX][1]), x[DOCT_NAME_IDX]))

def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """
    doctorsData,fileInfo = readFile(fileName)
    if fileInfo[FILETYPE] != "Doctors:":
        raise IOError(f"\n\nFile head error: scope inconsistency between name and header in file {fileName}.")
    doctorsData = sortDoctor(doctorsData)
    return doctorsData, fileInfo

def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.
    fileName is str with the name of a .txt file containing
    a list of requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Requires:
    list of lists where each list corresponds to a Mothers listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """
    requestsData,fileInfo = readFile(fileName)
    if fileInfo[FILETYPE] != "Mothers:":
        raise IOError(f"\n\nFile head error: scope inconsistency between name and header in file {fileName}.")
    newList = []
    for item in requestsData:
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
    requestsData = sorted(newList,key=lambda x: (-int(x[MOTH_IMP_IDK]),-int(x[MOTH_WRIST_IDK]),-int(x[MOTH_AGE_IDK]),x[MOTH_NAME_IDX]))
    return requestsData, fileInfo

def readScheduleFile(fileName):
    """
    Reads a file with a list of scheduled assistances with a given file name into a collection.
    fileName is str with the name of a .txt file containing
    a list of requests organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Requires:
    list of lists where each list corresponds to a Mothers listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """
    scheduleData,fileInfo = readFile(fileName)
    if fileInfo[FILETYPE] != "Schedule:":
        raise IOError(f"\n\nFile head error: scope inconsistency between name and header in file {fileName}.")

    return scheduleData, fileInfo
