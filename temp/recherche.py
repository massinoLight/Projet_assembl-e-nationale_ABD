import json
from atlassian import Jira
import configparser
import csv
import pandas as pd

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

JQL = "project = FOREVERZON AND Criticity =k2 AND created <= '2020-01-01'  order by created DESC"
csv_issuesK1 = jira.csv(
        jql=JQL, all_fields=False, )

with open("../data/temp.csv", "wb") as file_obj:
        file_obj.write(csv_issuesK1)
data = pd.read_csv("../data/temp.csv")
print(data)




"""
with open('test.csv', 'w') as f:
    for key in data.keys():
        f.write("%s,%s\n"%(key,data[key]))"""