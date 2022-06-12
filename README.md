# Using-Pyspark-to-extract-from-mysql-table-load-it-to-CSV

dependencies:
*You have to install Spark on your machine.
*you have add the mysql connector dependency jar to spark folder
    eg:C:\spark-3.0.3-bin-hadoop3.2\spark-3.0.3-bin-hadoop3.2\jars
    you can download it from:
    https://jar-download.com/artifacts/mysql/mysql-connector-java/8.0.11/source-code
    otherwise you can also uncomment the 1st 2 lines of the code.

Problem:
Assume you have a employee table with columns as emp_id, name,salary,date_of joining and address.
Use Pyspark to extract the data from Mysql and do Transformation like
address consists of atleast 4 words and salary is greater than 4000 and
load the result to CSV file.
