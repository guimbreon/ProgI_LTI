import infoFromFiles
#FILES
#DOCTORS
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/doctors14h00.txt"
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet4/doctors18h00.txt"
#REQUESTS
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/requests14h30.txt"
fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet1/requests10h30.txt"
#SCHEDULE
#fileName = "/home/guimbreon/Desktop/Aulas/Ano1/1Sem/PI/Trabalho/testSets_v1/testSet2/schedule14h00.txt"


#TESTING
#print(infoFromFiles.readDoctorsFile(fileName))
print(infoFromFiles.readRequestsFile(fileName))
#print(infoFromFiles.readScheduleFile(fileName))



"""
list = [["a",7],["b",12],["d",5],["c",4],["k",12],["d",12]]

print(sorted(list,key=lambda x: (x[1],x[0])))

my_list = [['Guilherme Gaspar', '2', [14, 20], '40', [39, 50]],
           ['Horácio Horta', '3', [15, 20], '120', [7, 20]],
           ['Ildefonso Inácio', '2', [15, 27], '40', [39, 50]],
           ['José Justo', '2', [9, 20], '40', [15, 0]]]

# Sort the list based on the third element and then the second element of each sublist
sorted_list = sorted(my_list, key=lambda x: (int(x[2][0]),int(x[2][1]), -int(x[1])))

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

sortedList = sorted(newList,key=lambda x: (-int(x[3]),-int(x[2]),-int(x[1]),x[0]))
print(sortedList)
"""