# ref from https://stackoverflow.com/questions/9574793/how-to-convert-a-python-datetime-datetime-to-excel-serial-date-number

import datetime as dt

def get_excel_date_serial_value(date1):
    date, month = date1.split("/")
    temp1 = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    temp2 = dt.datetime(1999, int(month), int(date))  
    delta = temp2 - temp1
    return float(delta.days) + (float(delta.seconds) / 86400)

