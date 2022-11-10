import sqlite3

def connect_db():
    global conn
    try:
        create_table = """ CREATE TABLE IF NOT EXISTS ru (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists ru_uni on ru (dest_lan, dest_text);                            
                              """
        conn = sqlite3.connect('translator.db')
        c = conn.cursor()
        c.executescript(create_table)
        conn.commit()

        return conn
    except sqlite3.Error as error:
        return error
