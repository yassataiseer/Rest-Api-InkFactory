import sqlite3
conn = sqlite3.connect('orders.db', check_same_thread=False)
c = conn.cursor()
class order_writer:##writes into orders.db
    def data_entry(order_data):
        order_data = order_data.split("+")
        c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(order_data[0],order_data[1],order_data[2],order_data[3],order_data[4],order_data[5],order_data[6],order_data[7],order_data[8],order_data[9],order_data[10],order_data[11],order_data[12],order_data[13]))  
        conn.commit()
    def data_fetcher():
        cursor = c.execute("SELECT * FROM stuffToPlot")
        orders = cursor.fetchall()
        return orders
    def ticket_builder():
        cursor = c.execute("SELECT order_No FROM stuffToPlot")
        number = cursor.fetchall()
        number = number[-1]
        for x in number :
            return int(x)+1
        
    def not_done_orders():
        package = []
        cursor = c.execute("SELECT * FROM stuffToPlot")
        orders = cursor.fetchall()
        for i in orders:
            if i[9]=="Completed":
                pass
            else:
                package.append(i)
        return package
    def order_finder(order_No):
        points = ["Order_No", "Client","Employee","Product","Model","Brand","Serial_No.","Accesory","Amount","Status","Description","Comments","Add_date","Up_date"]
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if order_No==rows[0]:
                send_data.append(rows)
            else:
                pass
            
        final = dict(zip(points,send_data[0]))
        return(final)
    def update_data(object):
        c.execute("SELECT client FROM stuffToPlot")
        a = c.fetchall()
        object = object.split("+")
        client = object[1]
        for row in a:
            if row[0]==client:
                ticket_data = object[0],client
                employee_data = object[2], client
                product_data = object[3],client
                model_data = object[4], client
                brand_data = object[5], client
                serial_no_data = object[6], client
                accessory_data = object[7], client
                amount_data = object[8],client 
                status_data = object[9],client
                description_data = object[10],client
                comments_data = object[11],client
                up_date_data = object[13], client
                c.execute('UPDATE stuffToPlot SET order_No = ?  WHERE client = ?;',ticket_data)
                c.execute('UPDATE stuffToPlot SET Employee = ?  WHERE client = ?;',employee_data)
                c.execute('UPDATE stuffToPlot SET product = ?  WHERE client = ?;',product_data)
                c.execute('UPDATE stuffToPlot SET model = ?  WHERE client = ?;',model_data)
                c.execute('UPDATE stuffToPlot SET brand = ?  WHERE client = ?;',brand_data)
                c.execute('UPDATE stuffToPlot SET serial_no = ?  WHERE client = ?;',serial_no_data)
                c.execute('UPDATE stuffToPlot SET Accessory = ?  WHERE client = ?;',accessory_data)
                c.execute('UPDATE stuffToPlot SET Amount = ?  WHERE client = ?;',amount_data)
                c.execute('UPDATE stuffToPlot SET Status = ?  WHERE client = ?;',status_data)
                c.execute('UPDATE stuffToPlot SET Description = ?  WHERE client = ?;',description_data)
                c.execute('UPDATE stuffToPlot SET Comments = ?  WHERE client = ?;',comments_data)
                c.execute('UPDATE stuffToPlot SET Up_date = ?  WHERE client = ?;',up_date_data)
                
                conn.commit()

