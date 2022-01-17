import sqlite3  #importing the sqlite library 
from tabulate import tabulate    #Using tabulate library for printing data in table format

# Connecting to the database
conn=sqlite3.connect('Movies.db')

# Creating the cursor
curs=conn.cursor()

# Creatign the table named as Movies
curs.execute("CREATE TABLE Movies (Name text,actor text, actress, director text, year of release integer)")

Data=[('Sholey','Amitabh','Malini','Ramesh',1975),('Bahubali','Prabhas','Anushka','Rajamouli',2016),('Vikram Vedha','Madhavan','Shraddha','Pushkar',2017),('KGF','Yash','Srinidhi','Prashanth',2018),('Marakkar','MohanLal','Keerthy',' Priyadarshan',2021),('Kabir Singh','Shahid','Kiara','Sandeep',2019),('Dil Bechara','Sushant','Sanjana','Mukesh',2020),('Avengers','Robert','Scarlett','Anthony',2019),('Pushpa','Arjun','Rashmika','Sukumar','2022'),('Magadhera','Charan','Kajal','Rajamouli',2010),('Avatar','Worthington','Saldana','Cameron',2019),('Pink','Amitabh','Tapsee','Anirudha',2016)]
# Inserting the data into the table 
curs.executemany("INSERT INTO Movies values (?,?,?,?,?)",Data)

# Fetching the data from the Movies Table
curs.execute("SELECT * FROM Movies")
results=curs.fetchall()

#  Printing the fetched data
print(tabulate(results,headers=['Name','Actor','Actress','Director','Year of Release'],tablefmt='orgtbl'))

# Fetching the data of a particular actor name here we have taken actor name as "Amitabh"
curs.execute("SELECT * FROM Movies where actor='Amitabh'")
print("\n\n\n")
results=curs.fetchall()
print(tabulate(results,headers=['Name','Actor','Actress','Director','Year of Release'],tablefmt='orgtbl'))

# Commit our commands
conn.commit() 

# Closing our connection
conn.close()
