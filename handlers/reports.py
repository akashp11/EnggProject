from flask_restful import Resource
from flask import render_template, make_response, send_from_directory, redirect, request
from models import PHCUser,medicaldata,reports,centreloc
from datastore import db
from datetime import datetime

class Reports(Resource):
    def get(self):
        list_reports=reports.query.order_by(reports.ReportTime.desc()).all()
        print(list_reports)
        for i in list_reports:
            print(i,"\n",i.ReportLoc,i.ReportTime)
        list_rep=[]
        for i in list_reports:
            rep_name="Report as on "+i.ReportTime.strftime("%d %b %Y")
            tmp={ 'ReportTime':i.ReportTime, 'ReportLoc':i.ReportLoc, 'ReportName':rep_name}
            list_rep.append(tmp)
        headers = {'Content-Type': 'text/html'}
        print(list_rep)
        return make_response(render_template('reports.html',reports=list_rep),200,headers)

class Output(Resource):
    def get(self,path):
        headers = {'Content-Type': 'text/html'}
        if("reports/" in path):
            print(path)
            return send_from_directory('',path)
        else:
            return make_response(render_template('error.html', errormsg="Access Denied"),200,headers)
        

def generate_report():
    
    print("Report Generated")
