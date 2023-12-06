import refresh
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


refresh.plan(fileNameDoctors,fileNameSchedule,fileNameRequests)