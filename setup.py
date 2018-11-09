from distutils.core import setup
setup(
	name = 'jira-issues-csv',
	version = '0.1',
	description = 'Automatic create jira issues using CSV files',
	author = 'Angelo Moura',
	author_email = 'angelo.moura@sec4you.com.br',
	url = 'https://github.com/sec4you/jira-issues-csv',
	download_url = 'https://github.com/sec4you/jira-issues-csv/archive/0.1.tar.gz',
	keywords = ['jira','csv'],
	install_requires = ['requests>=2.18.4'],
	classifiers = [],
	scripts = ['jira-issues-csv.py']
)
	
