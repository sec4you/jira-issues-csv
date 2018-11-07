from lib import JIRA
import argparse, csv


parser = argparse.ArgumentParser(description='')
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
        jira.create_issue(row['title'],row['subject'],project=row['project'],component=row['component'],assigne=row['assignee'])



