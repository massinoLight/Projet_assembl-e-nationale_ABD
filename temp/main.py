from atlassian import Jira
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
jira_server = config['SERVER']['host']
jira_user = config['LOGIN']['jira_user']
jira_password = config['LOGIN']['password']
token = config['LOGIN']['token']

jira = Jira(
        url=jira_server,
        username=jira_user,
        password=jira_password,
        cloud=True)


def getAllprojects():
    projects = jira.projects()
    return projects

def getproject(key) -> object:
    project=jira.get_project_components(key)
    print(project)


def getAllIssues(projectkey):
    issues = jira.get_project_issuekey_all(projectkey)
    return issues

if __name__ == '__main__':
    listkey=[]
    #print(getAllprojects())
    print(jira.user(jira_user))
    projets=getAllprojects()

    for i in range(0,len(projets)):
        print(projets[i])

    for i in range(0,len(projets)):
        listkey.append(projets[i]['key'])

    print(listkey)



#jira.get_project_versions_paginated(key, start=None, limit=None, order_by=None, expand=None, query=None, status=None)
