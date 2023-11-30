#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 13
# 62372 Guilherme Soares
# 62371 Duarte Soares




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










