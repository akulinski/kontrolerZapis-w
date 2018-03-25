from __future__ import print_function
import httplib2

from apiclient import discovery
from googleapiclient.http import MediaFileUpload

import getCredencials

import time
import modifyspreedsheet
import datetime



credentials = getCredencials.get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v3', http=http)

results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

def listFiles():
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

def upload():


    file_metadata = {'name': 'plan.xlsx','mimeType': 'application/vnd.google-apps.spreadsheet'}
    media = MediaFileUpload('plan.xlsx',mimetype='text/xlsx',resumable=True)

    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()

def delete(name):
    for item in items:
        if item['name']==name:
            service.files().delete(fileId=item['id']).execute()

def main():

    now = datetime.datetime.now()
    execDay=input("Podaj dzien w ktorym chcesz dokonac zamiany grafiku [eng i duza litera]")
    execHour=input("Podaj godzine")



    while 1:

        if str(execDay) == 'Sunday':
            print(execDay)
            print(now.hour)
            time.sleep(1)
            if str(now.hour) == str(execHour):
                upload()
                delete()

        else:
            print(localTime)


if __name__ == '__main__':
    main()