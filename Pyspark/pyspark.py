import findspark 
import mysql.connector
import os
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 
      
db = mysql.connector.MySQLConnection(
    host="localhost",
    user="root",
    password="Setiawan112!",
    database="proj0"
)

def getall():
  mycursor = db.cursor()
  mycursor.execute("Select * from users")
  result = mycursor.fetchall()
  print(result)
      
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
#df.show(1)
df1 = spark.read.option("header",True) \
     .csv("./users1.csv")
df1.createTempView("data")
spark.sql("select * from data where userid = '1'").show()

getall()
