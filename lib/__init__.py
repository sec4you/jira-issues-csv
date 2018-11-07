import requests, json
from requests.auth import HTTPBasicAuth
import logging

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

    def create_issue(self, title, subject, project, component=None, assigne=None):
        jdata = {}
        jdata['fields'] = {}
        fields = jdata['fields']
        fields['summary'] = title
        fields['description'] = subject
        fields['issuetype'] = {"name":"Task"}
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

