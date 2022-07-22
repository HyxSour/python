import pymysql
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='1234',
                       db='py_photo',
                       charset='utf8mb4')
print("连接成功")
cursor = conn.cursor()
fin = open(r"C:\Users\13287\PycharmProjects\pythonProject\1\阿卡丽\离群之刺.jpg", 'rb')
img = fin.read()
fin.close()
sql = "INSERT INTO photo VALUES (%s,%s);"   #将数据插入到mysql数据库中，指令
args = ('1', img)
cursor.execute(sql, args)                      #执行相关操作
conn.commit()                                 #更新数据库
#print(2)
cursor.close()
conn.close()
