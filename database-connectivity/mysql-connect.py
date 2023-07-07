import mysql.connector as mc
import testing1  as u

con = mc.connect (
    # hostname = u.hostname,
    user     = u.user,
    password = u.password
)

def __str__(m1):
    print(f"The      connection is made with the class object {m1}")
# connection= mc.connect(
#     host = "localhost",
#     user = "sud",
#     password = 'Sumo@1999'
# )

# # my_cursor = connection.cursor()

# # my_cursor.execute("show databases")

# # for i in my_cursor:
# #     print(i)
try:
    __str__(type(con).__name__)

    my_cursor = con.cursor()

    # my_cursor.execute("show databases")
    # for i in my_cursor:
    #     print(i)

    my_cursor.execute("use python_db")
    for i in my_cursor:
        print(i)
    # my_cursor.execute("describe py_table")
    # for i in my_cursor:
    #     print(i)
    # my_cursor.execute("show tables")
    # for i in my_cursor:
    #     print(i)
    # sql = "insert into py_table(c1, name) values (%s %s)"
    # val = [(1, "sudarshan"), (2, "Vijay"), (3, "Ajay")]
    # my_cursor.executemany(sql, val)
    # con.commit()
    my_cursor.execute("select * from py_table")
    for i in my_cursor:
        print(i)
   
except Exception as ex:
    print(ex)

con.close()

if con.close() != con:
    print("connected")
    __str__(type(con).__name__)
else:
    print("not connected") 
    __str__((con.close()))



