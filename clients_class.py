import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('clients.db', check_same_thread=False)
c = conn.cursor()


class client:
        def data():
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)
    def name_data():#gets name of person
        send_data=[]
        c.execute('SELECT name FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)
    def client_data(name):
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if name==rows[0]:
                send_data.append(rows)
            else:
                pass
        return(send_data)
    def clients_write(name,address1,address2,postcode,email,phone):
            c.execute("SELECT name FROM stuffToPlot")
            a = c.fetchall()
            for row in a:
                if row[0]==name:
                    address = address1,name
                    address102=address2,name
                    postalcode = postcode,name
                    mail = email,name
                    number = phone,name
                    c.execute('UPDATE stuffToPlot SET adress1 = ?  WHERE name = ?;',address)
                    c.execute('UPDATE stuffToPlot SET adress2 = ?  WHERE name = ?;',address102)
                    c.execute('UPDATE stuffToPlot SET postalcode = ?  WHERE name = ?;',postalcode)
                    c.execute('UPDATE stuffToPlot SET email = ?  WHERE name = ?;',mail)
                    c.execute('UPDATE stuffToPlot SET phone = ?  WHERE name = ?;',number)
                    conn.commit()