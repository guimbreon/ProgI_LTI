# 2023-2024 Programação 1 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62371 Duarte Soares

from constants import *
import copy
import infoFromFiles
import dateTime
def sortSchedule(schedule):
	"""
	Sort a schedule list.

    Requires:
    - schedule (lst)(lst) : contains a list of lists where each list  corresponds to an apointment.
    Ensures:
    New schedule list but now is sorted the given arguments.
	"""
	return sorted(schedule, key = lambda sched: (sched[0][0],sched[0][1]))

def updateSchedule(doctors, requests, previousSched, nextSched):
	"""
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	nextTime is a string in the format HHhMM with the time of the next schedule
	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability) and
	a list of doctors with their times updated after being sorted for a given birth.
	"""
	newRequests = []
	for sched in previousSched:
		if sched[0][0] == nextSched[0] and sched[0][1] >= nextSched[1] or sched[0][0] > nextSched[0]:
			
			newRequests.append(sched)
	schedule = copy.deepcopy(nextSched) #deepcopy so that the list can't be changed.
	for mother in requests:
		docNum = 0
		isItNotTreated = True
		for medic in doctors:
			if medic[DOCT_TIME_IDX] != "weekly leave": # if the "time" section of the given medic list is "weekly leave" it means it's not available to work anymore.
				if medic[DOCT_TIME_IDX][0] <= schedule[0] and medic[DOCT_TIME_IDX][1] < schedule[1] and isItNotTreated:
					medic[DOCT_TIME_IDX] = copy.deepcopy(schedule)
				copiedmedic = copy.deepcopy(medic)
				copiedmedic = dateTime.add20Min(copiedmedic)
				if copiedmedic != medic: 
					if ((int(mother[MOTH_IMP_IDX]) == 3 and int(medic[DOCT_CAT_IDX]) > 1) or (int(mother[MOTH_IMP_IDX]) < 3)) and isItNotTreated:
						isItNotTreated = False
						timeBegin = copy.deepcopy(medic[DOCT_TIME_IDX])
						medicName = copy.deepcopy(medic[DOCT_NAME_IDX])
						
						medic = dateTime.add20Min(medic)

						doctors.pop(docNum)
						doctors.append(medic)
						doctors = infoFromFiles.sortDoctor(doctors)
						newRequests.append([timeBegin,mother[MOTH_NAME_IDX],medicName])
			docNum += 1
		if isItNotTreated: #if the respective mother is not assigned to any doctor, it'll be redirected to other network.
			timeBegin = nextSched
			newRequests.append([timeBegin,mother[MOTH_NAME_IDX],"redirected to other network"])
		
	newRequests = sortSchedule(newRequests)
	doctors = sorted(doctors, key = lambda doctor:(doctor[DOCT_NAME_IDX]))
	
	return newRequests, doctors