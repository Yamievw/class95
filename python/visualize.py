from prettytable import PrettyTable
from random_table2 import *

import os
import webbrowser



schedule = random_table()
table = schedule.timetable


output = PrettyTable()




days = [" ", "Monday            ", "Tuesday             ", "Wednesday           ", "Thursday            ", "Friday          "]
slots = ["9:00 - 11:00", "11:00 - 13:00", "13:00 - 15:00", "15:00 - 17:00", "17:00 - 19:00"]


output.field_names = days



for timeslot in range(5):
    tmp = []
    for day in range(6):
        tmp_str = ""
        if day == 0:
            tmp.append(slots[timeslot])
        else:
            for activity in table[timeslot][day-1]:
                tmp_str += activity.name + " " + activity.ttype + "\n"
            tmp.append(tmp_str)
    output.add_row(tmp)
            






html = """ <!DOCTYPE html> <html> <head> <style> #table tr:nth-child(even){background-color: #f2f2f2;}
#customers {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

#customers td, #customers th {
    border: 1px solid #ddd;
    padding: 8px;
}



#customers tr:hover {background-color: #ddd;}

#customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #4CAF50;
    color: white;
}
</style></head><body> """
html += output.get_html_string(attributes={"id":"customers", "class":"table table-hover"})
print html
path = os.path.abspath('temp.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)
        



