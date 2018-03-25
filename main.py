from __future__ import print_function
import httplib2

from apiclient import discovery
import getCredencials

import time
import calendar
import datetime



credentials = getCredencials.get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v3', http=http)

results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

def upload():

    file_metadata = {'name': 'PLAN 6 SEMESTR.xlsx'}
    media = MediaFileUpload('files/plan.xlsx')

    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()

def delete(name):
    for item in items:
        if item['name']==name:
            service.files().delete(fileId=item['id']).execute()

def main():


    execDay=input("Podaj dzien w ktorym chcesz dokonac zamiany grafiku [eng i duza litera]")
    execHour=input("Podaj godzine")

    while 1:
        now = datetime.datetime.now()

        my_date = datetime.date.today()
        day=calendar.day_name[my_date.weekday()]
        if day == 'Thursday':
            print(day)
            time.sleep(1)
            if now.hour == execHour :

                delate()
                upload()
        else:
            print(localTime)

if __name__ == '__main__':
    main()