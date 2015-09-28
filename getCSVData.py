import csv
import math
from CSHLDAP import CSHLDAP
from gtts import gTTS 

your_gender_list = []
with open('match_scores.csv', 'rb') as f:
    reader = csv.reader(f)
    your_gender_list = list(reader)
    print(your_gender_list)
    tempList = [0] * len(your_gender_list)
    peopleList = [0] * len(your_gender_list)
    for x in range(len(your_gender_list)):
        tempList[x] = your_gender_list[x][1]
        peopleList[x] = your_gender_list[x][0]
    tempList[0] = -10
    finalPeopleList = []
    for x in range(len(peopleList)):
        name = peopleList[x].split("/") 
        nametemp = name[len(name) - 1]
        finalPeopleList += [nametemp]
    finalPeopleList[0] = ""
    print(finalPeopleList)
    index = min(range(len(tempList)), key=lambda i: abs(round(float(tempList[i]), 3)-11.5))
    print(finalPeopleList,tempList)
    base_dn = 'ou=Users,dc=csh,dc=rit,dc=edu'
    host = 'ldap://ldap.csh.rit.edu'
    password = '12-34-98'
    print("Prediction: ", finalPeopleList[index] , " Confidence: ", tempList[index])
    ldap_con = CSHLDAP("sherrardtr", password)
    result = ldap_con.search(cn=finalPeopleList[index].split('.')[0])
    msgString = "Hello " + finalPeopleList[index].split('.')[0]
    onFloor = result[0][1]['onfloor']
    skills =[]
    if('skills' in result[0][1]):
        skills = result[0][1]['skills']
    if(int(onFloor[0])):
        msgString += " you are an on floor member "
    else:
        msgString += " you are an off floor member "
    skillsStr = ""
    if(skills != []):
        for x in range(len(skills)):
            skillsStr +=  skills[x] + " " 
        msgString += "with skills in " + skillsStr 
    print(msgString)
    tts = gTTS(text=msgString, lang="en") 
    tts.save("hello.mp3")
            







        
    
    


