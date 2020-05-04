import sqlite3

con = sqlite3.connect("filePath" , isolation_level=None)
c = con.cursor()

c.execute("CREATE TABLE userInfo(id INTGER PRYMARY KEY, name text, age text , phone text)")

dbdata = (
  (1, "Seo", "25", "123"),
  (2, "Park", "22", "456"),
  (3, "Kim", "28", "789"),
  (4, "Beak", "24", "012"),
  (5, "Ko", "21", "345")
)

insert = "INSERT INTO userInfo(id , name, age, phone) VALUES(?,?,?,?)"

c.executemany(insert, dbdata)

con.close() 