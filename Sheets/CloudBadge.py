
from __future__ import print_function
import httplib2
import os
import datetime
from CloudUser import *
from WinStates import *

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
Users=[]

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



def get_sheet_values(credentials):
	http = credentials.authorize(httplib2.Http())
	discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
	service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

        #Test Sheet
        #spreadsheetId = '1uA8bHfl6I7lBPOMGvOkJFwJ4Zidf0olTMHPLC5F17ww'
        spreadsheetId ='1n0aWJTFSEtBBq8Ud8dC1JrgYIseuYJfwktmd4hj4_Ts'
	sheet_tabName = get_tab_date()
	#rangeName = sheet_tabName + '!A3:C'
        rangeName = sheet_tabName + '!B4:D'
	result = service.spreadsheets().values().get(
        	spreadsheetId=spreadsheetId, range=rangeName).execute()


	return result.get('values', [])


def parse_username(name_line):
        uname=''
        if(name_line.index('(')):
            uname_index=name_line.index('(') + 1
            uname = name_line[uname_index:].rstrip(')')
        
	return uname


def populate_users(big_list):
        for row in big_list:
	    if(len(row)<3):
               continue

            if(row[0] == ""):
                continue
            if(row[0] == "Name"):
                continue

	    uname=parse_username(row[0])
	    count=len(row[1])
	    cases=row[2].split(',')
            #CloudUser(uname,count,cases)  
	    Users.append(CloudUser(uname,count,cases))


def get_tab_date():
	date = datetime.date.today()
	return str(date.month)+"/"+str(date.day)


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    values = get_sheet_values(credentials)
    populate_users(values)
    for each in Users:
        check_wins(each)
        print(each)

if __name__ == '__main__':
    main()


