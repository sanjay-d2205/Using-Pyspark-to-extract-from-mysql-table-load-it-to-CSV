# Using-Pyspark-to-extract-from-mysql-table-load-it-to-CSV
<br />
dependencies:<br />
*You have to install Spark on your machine.<br />
*you have add the mysql connector dependency jar to spark folder <br />
    eg:C:\spark-3.0.3-bin-hadoop3.2\spark-3.0.3-bin-hadoop3.2\jars <br />
    you can download it from:<br />
    https://jar-download.com/artifacts/mysql/mysql-connector-java/8.0.11/source-code <br />
    otherwise you can also uncomment the 1st 2 lines of the code.<br />
<br />
Problem:<br />
Assume you have a employee table with columns as emp_id, name,salary,date_of joining and address.
Use Pyspark to extract the data from Mysql and do Transformation as
address consists of atleast 4 words and salary is greater than 4000 and
load the result to CSV file.
