#!/usr/bin/env python

import requests, json                                                                                                                 
from requests.auth import HTTPBasicAuth
import logging
import argparse, csv

logging.basicConfig(level='DEBUG')

class JIRA(object):
    def __init__(self,url=None,username=None,password=None):
        self.url = url
        self.username = username
        self.password = password

    def get_projects(self):
        req = requests.get("{}/rest/api/2/project".format(self.url),
                            auth = HTTPBasicAuth('{}'.format(self.username), '{}'.format(self.password))
                           )
        try: return json.loads(req.text)
        except: return req.text

    def get_project_by_name(self, name):
        projects = self.get_projects()
        project = filter(lambda d: d['name'] == name, projects)
        return project

    def get_project_by_key(self, key):
        projects = self.get_projects()
        project = filter(lambda d: d['key'] == key, projects)
        return project

    def get_components_by_project_key(self, key):
        req = requests.get("{}/rest/api/2/project/{}/components".format(self.url, key),
                           auth=HTTPBasicAuth('{}'.format(self.username), '{}'.format(self.password))
                          )
        try: return json.loads(req.text)
        except: return req.text

    def create_issue(self, title, subject, project, issue_type=None, component=None, assigne=None):
        jdata = {}
        jdata['fields'] = {}
        fields = jdata['fields']
        fields['summary'] = title
        fields['description'] = subject
        fields['issuetype'] = {"name":issue_type if issue_type else "New Feature"}
        fields['project'] = {"key":project}
        if component:
            c = filter(lambda d: d['name'] == component,
                         self.get_components_by_project_key(project)
                       )
            if c: component = [{"id": c[0]['id']}]
            fields['components'] = component
        if assigne: fields['assignee'] = {"name":assigne}
        logging.debug(jdata)
        issue = requests.post("{}/rest/api/2/issue".format(self.url),
                      json=jdata,
                      auth = HTTPBasicAuth('{}'.format(self.username), '{}'.format(self.password))
                      )                                                                                                                                                                                                                                                       
        return issue

parser = argparse.ArgumentParser(description='jira-issues-csv')
parser.add_argument('--url', help='JIRA URL (example: https://jira.acme.com.br)', required=True)
parser.add_argument('--username', help='JIRA Usernanme', required=True)
parser.add_argument('--password', help='JIRA Password', required=True)
parser.add_argument('--csv', help='CSV File with issues to import on JIRA', required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    jira = JIRA(url=args.url,username=args.username,password=args.password)
    print jira.get_projects()
    csvfile = open(args.csv)
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        jira.create_issue(row['title'],row['subject'],project=row['project'],issue_type=row['type'],component=row['component'],assigne=row['assignee'])



