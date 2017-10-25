import csv

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def gsheet2csv(keyfile_path, spreadheet_title, worksheet_name, csv_path):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)
    gc = gspread.authorize(credentials)

    wks = gc.open(spreadheet_title).worksheet(worksheet_name)
    data = wks.get_all_values()

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data)
