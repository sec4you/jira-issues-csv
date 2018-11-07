# Issue Manager

### Requirements

`pip install requests`

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
title;subject;project;component;assignee
Test1;Test subject;github;user
```
