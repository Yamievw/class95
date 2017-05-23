from prettytable import PrettyTable
import os
import webbrowser




def visualize(table, room=False):
    try:
        table = table.timetable
    except:
        pass 
    output = PrettyTable()

    days = [" ", "Monday                  ", "Tuesday                 ", "Wednesday                ", "Thursday                     ", "Friday                "]
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
                    if activity.ttype == "lectures":
                        tmp_str += activity.name + " (" + activity.ttype + " " +  " in " + activity.room.name + ") "
                    else:
                        tmp_str += activity.name + " (" + activity.ttype + " " + str(activity.group_id) + " in " + activity.room.name + ") "

                    if room:
                        tmp_str += activity.room
                    tmp_str += "\n"
                tmp.append(tmp_str)
        output.add_row(tmp)
                






    html = """ <!DOCTYPE html> <html> <head> <style>
    #customers tr:nth-child(even){background-color: #f2f2f2;}
    #customers {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    #customers td, #customers th {
        border: 1px solid #ddd;
        padding: 8px;
    }

    td {
        line-height: 150%;
    }


    #customers td:hover {background-color: #ddd;}

    #customers th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #6495ED;
        color: white;
    }
    </style></head><body> """
    html += output.get_html_string(attributes={"id":"customers", "class":"table table-hover"})
    path = os.path.abspath('temp.html')
    url = 'file://' + path

    with open(path, 'w') as f:
        f.write(html)
    webbrowser.open(url)

