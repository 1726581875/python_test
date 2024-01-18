import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="test"
)

# 创建游标对象
cursor = conn.cursor()

# 插入数据
insert_query = "INSERT INTO xmz_table (id, name) VALUES (%s, %s)"
values = ("1", "张三")
cursor.execute(insert_query, values)
conn.commit()
# 插入数据
insert_query = "INSERT INTO xmz_table (id, name) VALUES (%s, %s)"
values = ("2", "李四")
cursor.execute(insert_query, values)
conn.commit()
print("数据插入成功")

# 更新数据
update_query = "UPDATE xmz_table SET name = %s WHERE id = %s"
new_value = "张三丰"
condition = "2"
cursor.execute(update_query, (new_value, condition))
conn.commit()
print("数据更新成功")

# 删除数据
delete_query = "DELETE FROM xmz_table WHERE id = %s"
delete_value = "1"
cursor.execute(delete_query, (delete_value,))
conn.commit()
print("数据删除成功")

# 查询数据
select_query = "SELECT id,name FROM xmz_table"
cursor.execute(select_query)
result = cursor.fetchall()
for row in result:
    print(row)
    print("id="+ str(row[0]) + ", name=" + row[1])

# 关闭游标和连接
cursor.close()
conn.close()
