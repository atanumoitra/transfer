import pandas as pd
import pyodbc
import psycopg2

#connect to your SQL server
server = 'your SQL server deatail' 
database = 'your_db' 
username = 'your_user_name' 
password = 'your_password' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#put your data into dataframe
df = pd.read_sql_query("SELECT Id,RoleName,RoleCode,IsActive FROM [BSK].[bsk].[mst_Roles]", cnxn)
cnxn.close()

print(df)

#connect to your postgresql
connpg = psycopg2.connect(
   database="your_postgre_db", user='postgray_user', password='postgray_password', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = connpg.cursor()

for i in df.index:
    sql = "INSERT INTO dbo.mst_Roles(roleId,RoleName,RoleCode,IsActive) VALUES (%s, %s, %s, %s)"
    val = (str(df['Id'][i]), str(df['RoleName'][i]),str(df['RoleCode'][i]),str(df['IsActive'][i]))
    cursor.execute(sql, val)
    connpg.commit()

connpg.close()
