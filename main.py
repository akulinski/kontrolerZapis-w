from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import getCredencials

import time
import calendar
import datetime


def upload():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials =getCredencials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))


def main():

    while 1:
        now = datetime.datetime.now()

        my_date = datetime.date.today()
        day=calendar.day_name[my_date.weekday()]
        if day == 'Thursday':
            print(day)
            time.sleep(1)
            print(str(now.hour)+" "+str(now.minute))
        else:
            print(localTime)

if __name__ == '__main__':
    main()