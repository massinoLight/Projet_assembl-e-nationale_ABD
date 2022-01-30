from main import getAllprojects
from main import jira

projets=getAllprojects()
key=[]
print("*******************************************")
for i in range(0,len(projets)):
    key.append(projets[i]['key'])
print(key)

total=[]
for j in range(0,len(key)):

    JQL = "project ="+ key[j]
    data = jira.jql(JQL)
    total.append(data["total"])



print(total)