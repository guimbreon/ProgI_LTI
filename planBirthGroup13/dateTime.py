#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 13
# 62372 Guilherme Soares
# 62371 Duarte Soares
from constants import * 
def nextDay(date):
    """
    It skips to the next day in the given string

    Requires:
    - date(str) : representing a given day.
    Ensures:
    date(str) + 1 day, representing the next day
    """
    date = date.split(":")
    day = int(date[DAY])
    month = int(date[MONTH])
    year = int(date[YEAR])
    if day == 30:
        day = 1
        if month == 12:
            month = 1
            year = year + 1
        else:
            month = month + 1
    else:
        day = day + 1
        month = month
        year = year
    return f"{day}:{month}:{year}\n"


def hourToInt(time):
    """
    Transforms give time str into an int.
    
    Requires:
    - time (str): representing a given time in  the format "HHhMM".
    Ensures: 
    - int: representing only the hours in the given time.
    """
    t = time.split("h")
    return int(t[0])



def minutesToInt(time):
    """
    Transforms give time str into an int.
    
    Requires: 
    - time (str): representing a given time in  the format "HHhMM".
    Ensures: 
    - int: representing only the minutes in the given time.
    """
    t = time.split("h")
    return int(t[1])
    


def intToTime(hour, minutes):
    """
    Transforms hour and minutes (integers) into a time String.

    Requires: 
    - hour (int): representing hours
    - minutes (int): representing minutes
    Ensures:
    -str: representing the time in the format "HHhMM".

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m










