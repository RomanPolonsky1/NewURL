import sqlite3

conn = sqlite3.connect('test.db')
print("Opened/Created database success")

conn.execute('''CREATE TABLE ShortURL
         (REAL_URL           TEXT    NOT NULL,
         SHORT_URL        TEXT    NOT NULL,
         TITLE                      TEXT);''')

# conn.execute("INSERT INTO ShortURL (REAL_URL,SHORT_URL) \
#       VALUES ('www.test.com', '32')");

cursor = conn.execute("SELECT * from ShortURL")

for item in cursor:
    print(item)

another = conn.execute("SELECT REAL_URL FROM ShortURL WHERE SHORT_URL=?", (321,))
print(another.fetchone())
conn.commit()

conn.close()