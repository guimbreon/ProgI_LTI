#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62371 Duarte Soares
import dateTime
from constants import * 

def headerWork(header):
    lineNum = 0
    nextDay = False
    headerString = ""
    for line in header:
        if lineNum == 3:
            hour = dateTime.hourToInt(line)
            min = dateTime.minutesToInt(line) + 30
            if min == 60:
                hour = hour + 1
                min = 0
            if hour > 24:
                hour = 1
                nextDay = True
            headerString += dateTime.intToTime(hour,min) + "\n"
        elif nextDay and lineNum == 5:
            headerString += dateTime.nextDay(line)
        else:        
            headerString += line
        lineNum += 1

    return headerString
    


def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    fp = open(fileName,'w')
    fp.write(header)
    for item in sched:
        fp.write(f"{dateTime.intToTime(item[REQ_TIME_IDX][0],item[REQ_TIME_IDX][1])}, {item[REQ_MOTH_IDX]}, {item[REQ_DOC_IDX]}\n")

    fp.close()
def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a collection of doctors after the assistances into a file.

    Requires:
    doctors is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the doctors after the assitances,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    fp = open(fileName,'w')
    fp.write(header)
    for item in doctors:
        fp.write(f"{item[DOCT_NAME_IDX]}, {item[DOCT_CAT_IDX]}, {dateTime.intToTime(item[DOCT_TIME_IDX][0],item[DOCT_TIME_IDX][1])}, {item[DOCT_MINS_IDX]}, {dateTime.intToTime(item[DOCT_TOTALTIME_IDX][0],item[DOCT_TOTALTIME_IDX][1])}\n")

    fp.close()