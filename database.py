#!/usr/bin/python3

import sqlite3

def main():
    #create the database
    db = sqlite3.connect('address.db')

    #create the table
    db.execute('drop table if exists address')
    db.execute('create table address' (fname varchar(25), lname varchar(35), address
varchar(35), city varchar(35), state varchar(2), zip varchar(10), phone
varchar(10)))
    
    #add data to the database
    db.execute('insert into address' (fname, lname, address, city, state, zip,
phone) values (?, ?, ?, ?, ?, ?, ?)', ('John', 'Doe', '123 Any St.', 'Anywhere',
'CA', 59246, 5609865231))
    db.execute('insert into address' (fname, lname, address, city, state, zip,
phone) values (?, ?, ?, ?, ?, ?, ?)', ('Jane', 'Doe', '123 Any St.', 'Anywhere',
'CA', 59246, 5609865231))
    db.execute('insert into address' (fname, lname, address, city, state, zip,
phone) values (?, ?, ?, ?, ?, ?, ?)', ('George', 'Jungle', '45 Banana Gr.',
'Hollywood', 'CA', 59286, 5607894561))
    db.execute('insert into address' (fname, lname, address, city, state, zip,
phone) values (?, ?, ?, ?, ?, ?, ?)', ('Benjamin', 'Pierce', '', 'Crabapple Cove',
'ME', 95123, 2036589523))
    db.commit()

    #retrieve and display the data
    cursor = db.execute('select * from address order by lname')
    for row in cursor:
        print(row)
    
    #print extra row to separate output
    print("")

    #delete a row
    db.execute('delete from address where fname = ?', ('John',))
    db.commit()

    #retrieve and display the data again
    cursor = db.execute('select * from address order by lname')
    for row in cursor:
        print(row)

if __name__ == "__main__": main()
