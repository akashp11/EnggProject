from flask_restful import Resource
from flask import render_template, make_response, send_from_directory, redirect, request
from models import reports,algorithms
from datastore import db
from datetime import datetime
import os
from handlers.corona import get_table_in_html, get_moving_average_growth_rate_and_prediction
def gen_coronavirus_report(launch_method,al):
    get_table_in_html('covid_19_india.csv')
    get_moving_average_growth_rate_and_prediction('covid_19_india.csv')
    currtime=datetime.strptime(datetime.now().strftime("%Y %m %d 00 00 00"),"%Y %m %d %H %M %S")
    filename="coronavirus_reports/"+currtime.strftime("%Y-%m-%d_00-00-00")+".html"
    filename1=os.getcwd()+filename
    if(al==None):
        rep=reports(ReportTime=currtime,ReportLoc=filename)
    else:
        rep=reports(ReportTime=currtime,ReportLoc=filename,Algorithm=al)
    db.session.add(rep)
    db.session.commit()
    print("Reports generated")
