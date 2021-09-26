import sqlite3

connection = sqlite3.connect("data.db")

# to get cursor of something like dictionary instead of a tuple (by default we are getting a tuple)
# i.e to use the commented out line in view_entries function of app.py
# connection.row_factory = sqlite3.Row  

def create_table():
    # connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    # connection.commit()
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    # !!! High risk - SQL Injection Attack
    #with connection:
        # connection.execute(f"INSERT INTO entries VALUES('{entry_content}, {entry_date}');")
        
    # The Fix
    with connection:
        connection.execute(f"INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date))
    
def get_entries():  
    #connection.execute("SELCT * FROM entries;") # automatically creates cursor for... it can be returned as well
    cursor = connection.execute("SELECT * FROM entries;") # to give it all back to the cursor
    #return cursor.fetchall()
    return cursor # we can just return the cursor as it is smart enough to fetch all rows for us

    # another way
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries")
    # return cursor