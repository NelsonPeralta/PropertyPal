import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd = "", database="new_python_db")

cur = db.cursor()



# ***** INSERT example *****

# cur.execute("INSERT INTO members (company_id, username, password) VALUES (%s, %s, %s)", (1, "a_username", "a_password"))
# db.commit()

# **************************



# ***** SELECT example *****

# params = {
#     "company_id":1,
#     "username" : "a_username",
#     "password" : "a_password"
# }

# sqlnom=("SELECT * FROM members WHERE username=%s and password=%s")
# adr=("a_username", "a_password")
# cur.execute(sqlnom, adr)

# myresult = cur.fetchall()

# for x in myresult:
#   print(x)

# **************************