import sqlite3
'''
Модуль подключения к базе данных и создания таблиц для языков 

'''

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
                             
                             CREATE TABLE IF NOT EXISTS be (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists be_uni on be (dest_lan, dest_text);
                             
                             CREATE TABLE IF NOT EXISTS uk (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists uk_uni on uk (dest_lan, dest_text);   
                             
                             CREATE TABLE IF NOT EXISTS en (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists en_uni on en (dest_lan, dest_text);
                             
                             CREATE TABLE IF NOT EXISTS de (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists de_uni on de (dest_lan, dest_text); 
                             
                             CREATE TABLE IF NOT EXISTS fr (
                                               id integer PRIMARY KEY NOT NULL,
                                               origin_text varchar,
                                               dest_lan varchar,
                                               dest_text varchar
                                           ); 
                             create unique index if not exists fr_uni on fr (dest_lan, dest_text);                                       
                              """
        conn = sqlite3.connect('translator.db')
        c = conn.cursor()
        c.executescript(create_table)
        conn.commit()

        return conn
    except sqlite3.Error as error:
        return error
