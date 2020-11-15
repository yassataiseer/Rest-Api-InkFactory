import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('employees.db', check_same_thread=False)
c = conn.cursor()

class employees:
    def validate_user(users):
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        for rows in data:
            if users[0]==rows[2] and users[1]==rows[3]:
                return True
    def Certain_Employee_Data(email):
        points = ["First Name", "Last Name","Email","Password","Add Date","New Date"]
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if email==rows[2]:
                final = dict(zip(points,rows))
                send_data.append(final)            
            else:
                pass
        return(send_data)
    def write(firstname,lastname,email,password,newdate):
        c.execute("SELECT Email FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            if row[0]==email:
                fname = firstname,email
                lname = lastname,email
                password_edit=password,email
                date_changer = newdate,email
                c.execute('UPDATE stuffToPlot SET firstname = ?  WHERE Email = ?;',fname)
                c.execute('UPDATE stuffToPlot SET lastname = ?  WHERE Email = ?;',lname)
                c.execute('UPDATE stuffToPlot SET password = ?  WHERE Email = ?;',password_edit)
                c.execute('UPDATE stuffToPlot SET newdate = ?  WHERE Email = ?;',date_changer)
                conn.commit()
        











