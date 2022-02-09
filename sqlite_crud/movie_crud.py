import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('movies.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE movies(
        movie_name text,
        actor_name text,
        actress_name text,
        release_year text,
        director_name text
    )""")

# ####### insert record into table #######
many_records = [
    ('The Father', 'Anthony Hopkins', 'Olivia Colman', '2021', 'Florian Zeller'),
    ('Dune', 'Timothée Chalamet', 'Zendaya', '2021', 'Denis Villeneuve'),
    ('Minari', 'Steven Yeun', 'Youn Yuh-jung', '2021', 'Lee Isaac Chung')
]
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", many_records)
# we can insert only one record
c.execute("INSERT INTO movies VALUES ('First Man', 'Ryan Gosling', 'Claire Foy', '2018', 'Damien Chazelle')")

# ###### Update records into the table ######
'''c.execute("""UPDATE movies SET release_year='22 October 2021'
    WHERE rowid = 2
    """) '''

# #### Delete record into the table ####
''' c.execute("DELETE from movies WHERE rowid=4") '''

# Drop table
''' c.execute("DROP TABLE movies") '''

# Query The Database
c.execute("SELECT rowid, * FROM movies")
# print(c.fetchone())
# print(c.fetchmany(3))
# fetch and print all records of the table
items = c.fetchall()
# print(items)
for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()
