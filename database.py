import mysql.connector
from mysql.connector import Error
import sqlite3

def disease(y):
  
    connection = sqlite3.connect('sample.db')
    sql_select_Query = "select * from intensity1"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
  
    x1=records[0][1]S
    x2=records[1][1]
    x3=records[2][1]
    x4=records[3][1]

    if(y>=x1-0.5 and y<=x1+0.5):
      print("Disease Name: ",records[0][0]);
      
    elif(y>=x2-0.5 and y<=x2+0.5):
      print("Disease Name: ",records[1][0]);
          
    elif(y>=x3-1 and y<=x3+1):
      print("Disease Name: ",records[2][0]);
        
    elif(y>=x4-1 and y<=x4+1 ):
      print("Disease Name: ",records[3][0]);

    elif(y>=3 and y<=5.5 or y>=33 and y<=60):
      print("Leaf is Suffering from Disease")	
      print("Disease Name: ","Soon Disease Name should be in our Database");
        
    else:
      print("No Disease Detected");    

