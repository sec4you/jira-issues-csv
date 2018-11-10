# Issue Manager

### Installation

- From source:

```
git clone https://github.com/sec4you/jira-issues-csv
cd jira-issues-csv
python setup.py install
```

- From source with pip:

```
git clone https://github.com/sec4you/jira-issues-csv
cd jira-issues-csv
python setup.py sdist
pip install dist/*
```

### Usage

```
usage: issuemanager.py [-h] --url URL --username USERNAME --password PASSWORD
                       --csv CSV

optional arguments:
  -h, --help           show this help message and exit
  --url URL            JIRA URL (example: https://jira.acme.com.br)
  --username USERNAME  JIRA Usernanme
  --password PASSWORD  JIRA Password
  --csv CSV            CSV File with Issue to import on JIRA
```

### CSV File example

```
title;subject;project;type;component;assignee
Test1;Test subject;Issue type;Test component;Test user
```

- Mandatory: title, subject, project

- Optional: type, component, assignee


