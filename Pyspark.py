#import findspark
#findspark.add_packages('mysql:mysql-connector-java:8.0.11')

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql.functions import col

dataframe_mysql = spark.read.format("jdbc").options(
    url="jdbc:mysql://localhost/students", #students is database name
    driver = "com.mysql.jdbc.Driver",
    dbtable = "employee", #employee is table name
    user="root",
    password="password").load()

dataframe_mysql.show()

filt=dataframe_mysql.filter("salary> 4000")
filt.show()

resdf=filt.filter(col("address").like("% % % %"))
resdf.show()

resdf.write.csv("datacsv", header=True)