from flask import Flask, render_template
from datetime import  timedelta, datetime
from getDateContrat import getdateContrat
from getIssusFrequency import getIssusFrequence
#to do ajouter des filtre pour k1 +k2 + k3 + k4
coedOD = ["OD2000846",   "OD1701110", "OD2100100", "OD2000655", "????"]
projets=["FOREVERZON", "XDD",    "echo",     "HCB", "CMFB-EV"]



#getIssusFrequence("FOREVERZON",getdateContrat("OD1501612"))
#getIssusFrequence("FOREVERZON",getdateContrat("OD1501612")- timedelta(20))


app = Flask(__name__)



def getfreq(projet):
    data = []
    Closed = []
    To_be_Documented = []
    PO_Reviewing = []
    To_be_Decided = []
    Draft = []
    To_be_Specified = []
    To_be_Checked = []
    total = []
    date = []
    dateweek = []
    for i in range(0, 10):
        data.append(getIssusFrequence(projet, datetime(2021, 10, 12, 0, 0) - timedelta(i * 10)))

    for i in range(len(data) - 1, -1, -1):
        week = datetime.fromisoformat(str(data[i]['date'])[0: 10: 1]).isocalendar()[1]
        year = str(data[i]['date'])[2: 4: 1]
        dateweek.append(year + " W " + str(week))

        date.append(data[i]['date'])
        Closed.append(data[i]['Closed'])
        To_be_Documented.append(data[i]['To be Documented'])
        PO_Reviewing.append(data[i]['PO Reviewing'])
        To_be_Decided.append(data[i]['To be Decided'])
        Draft.append(data[i]['Draft'])
        To_be_Specified.append(data[i]['To be Specified'])
        To_be_Checked.append(data[i]['To be Checked'])
        total.append(data[i]['total'])

    dateweek[len(date) - 1] = str(date[len(date) - 1]) + " CO"
    return date,dateweek,Closed,To_be_Documented,PO_Reviewing,To_be_Decided,Draft,To_be_Specified,To_be_Checked,total


@app.route('/')
def index():
    return render_template('main.html')



@app.route('/forever', methods=['GET', 'POST'])
def forever():

    date,dateweek,Closed,To_be_Documented,PO_Reviewing,To_be_Decided,Draft,To_be_Specified,To_be_Checked,total=getfreq("FOREVERZON")

    return render_template('home.html', labels=projets[0], title="Ki from Jira", date=dateweek, Closed=Closed,
                           To_be_Documented=To_be_Documented,
                           PO_Reviewing=PO_Reviewing, To_be_Decided=To_be_Decided, Draft=Draft,
                           To_be_Specified=To_be_Specified, To_be_Checked=To_be_Checked, total=total)


@app.route('/contact')
def contact():
    return render_template('contact.html')