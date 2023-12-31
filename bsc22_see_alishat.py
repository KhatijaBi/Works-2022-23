# -*- coding: utf-8 -*-
"""BSc22_SEE_alishat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TZCw0j9gWI_8fV0QOgqTg6J1JIKMT0Ge

<center><h3> RV University </h3></center>   
<center><h4> SEE B.Sc.22: DBMS </h4></center>
<pre>
        Date: 12 June 2023                   Duration: 3 hours                  Max Marks: 30
</pre>

---

#### Instructions   
1. Answer only for 30 marks  
2. Turn-off you mobile phones and keep them away. If your phone is connected to the WIFI, your PC may not get good connection which will affect your performance in the exam. 
3. You may refer to the Internet as well to your iPython notebooks.  
4. Copying from other students or sharing screen with them is not allowed. 
5. All your work should be done using 'BSc22_SEE_\<your folder name\>.ipynb', uploaded to your folder. Only the contents in this notebook and the resultant database and database tables in your folder will be evaluated. 
6. Because an auto-grader will be used to evaluate your work, **proper naming of the database, tables, and columns is important**.  
    . Using markdown cells before the code cells, write documentation for your implementation.  
    . Use meaningful variable names.   
    . The auto-grader will check the metadata in the database, source code and documentation in the notebooks.   
7. **Do not clear the outputs of executions in your notebooks**. They are required for evaluation. 

#### Warning      
**Those found consulting others by using email, chat, call, or screen sharing may be debarred**.

Go to your shared folder and find the following:     
1. 'BSBT22_Electives.xlsx' data file. Only for reference.    
2. 'BSc22_SEE_\<your folder name\>.ipynb' to write all your code.   
3. 'BSc22_SEE_\<your folder name\>.sqlite' to create your tables, populate, and work on them.   
    This database already has a table named BSBT22_Electives.

---
#### Tasks Level 1 - Queries on table BSBT22_Electives   
<pre>
1.                                                                                       2
    a) Find the count of rows in the table  
    b) Display data on all the columns on 5 rows starting from the 100th row   
    c) Display Name, Course, Section, and Elective for the first 5 rows   
</pre>
"""

#  import modules  
import pandas as pd
import os
import sqlite3 as lite
import csv
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# mount google drive
from google.colab import drive
drive.mount('/content/drive',force_remount=True)
os.chdir('/content/drive/My Drive/alishat/')
print(os.getcwd())

# count of rows
conn = lite.connect('BSc22_SEE_alishat.sqlite')
cur = conn.cursor()

# a) Find the count of rows in the table
cur.execute("SELECT COUNT(*) FROM BSBT22_Electives")
row_count = cur.fetchone()[0]
print("Row count:", row_count)

# Name, Course, Section, and Elective for the first 5 rows
cur.execute("SELECT * FROM BSBT22_Electives LIMIT 5 OFFSET 99")
rows = cur.fetchall()
print("Data on all columns for 5 rows starting from the 100th row:")
for row in rows:
    print(row)

"""<pre>
2.                                                                                      2
    a) Print rows Name, Course, Section, and Elective for students 
       who have chosen 'Kuchipudi' as elective. 
    b) Print the count of students 
       who have chosen an elective which has 'Leadership' as part of its name. 
</pre>    
"""

# records with Kuchipudi as elective

con = lite.connect('BSc22_SEE_alishat.sqlite')
cur = conn.cursor()

cur.execute("SELECT Name, Course, Section, Elective FROM BSBT22_Electives WHERE Elective = 'Kuchipudi'")
rows = cur.fetchall()
print("Name, Course, Section, and Elective for students who have chosen 'Kuchipudi' as elective:")
for row in rows:
    print(row)

# records with Leadership as elective
cur.execute("SELECT COUNT(*) FROM BSBT22_Electives WHERE Elective LIKE '%Leadership%'")
count = cur.fetchone()[0]
print("Count of students who have chosen an elective with 'Leadership' in its name:", count)

"""<pre>
3.                                                                                     4
    a) Print elective name and count of students for each elective  
             sorted by the count in descending order and 
             column header for count named as 'Students'. 
    b) Print elective name, course, section, and count of students for each elective  
             for BSc section A 
             sorted by the count in descending order and 
             column header for count named as 'Students'. 
</pre>    
"""

# elective name and count of students for each elective
con = lite.connect('BSc22_SEE_alishat.sqlite')
cur = conn.cursor()

cur.execute("SELECT Elective, COUNT(*) AS Students FROM BSBT22_Electives GROUP BY Elective ORDER BY Students DESC")
rows = cur.fetchall()
print("Elective Name and Count of Students for Each Elective:")
for row in rows:
    print(f"{row[0]} \t {row[1]}")

# elective name and count of students for each elective for BSc. Section A
con = lite.connect('BSc22_SEE_alishat.sqlite')
cur = conn.cursor()

cur.execute("SELECT Elective, Course, Section, COUNT(*) AS Students FROM BSBT22_Electives  WHERE Course = 'BSc' AND Section = 'A' GROUP BY Elective ORDER BY Students DESC")
rows = cur.fetchall()
print("Elective Name, Course, Section, and Count of Students for Each Elective (BSc Section A):")
print("Elective Name\tCourse\tSection\tStudents")
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t{row[3]}")

"""##### Note   
After changes to database, 
commit the changes, close the database,   
open again and confirm that the changes are persisted. 

<pre>
4.                                                                                     8
    a) Insert 4 new rows into BSBT22_Electives.  
       Check the new row counts.  
       Verify the newly inserted records by displaying them.  
    b) Add column 'Credits' and insert default value of 2.     
       Verify that the insertions have been effected. 
    c) Delete the rows inserted at a)   
       commit and vacuum the database.   
       Check the new row counts.  
       Verify that the deleted records do not display.  
    d) Delete the column inserted at b)   
       commit and vacuum the database.   
       Check the column.  
       Verify that Counts column is deleted.  
    
</pre>  
"""

# insert 4 new rows and verify  
con = lite.connect('BSc22_SEE_alishat.sqlite')
cur = con.cursor()

new_rows = [
    ('Elective1', 'Course1', 'Section1', 'Name1', 'Male'),
    ('Elective2', 'Course2', 'Section2', 'Name2', 'Female'),
    ('Elective3', 'Course3', 'Section3', 'Name3', 'Male'),
    ('Elective4', 'Course4', 'Section4', 'Name4', 'Female')
]
cur.executemany("INSERT INTO BSBT22_Electives (Elective, Course, Section, Name, Sex) VALUES (?, ?, ?, ?, ?)", new_rows)

cur.execute("SELECT COUNT(*) FROM BSBT22_Electives")
row_count = cur.fetchone()[0]
print("Row count after insertion:", row_count)

cur.execute("SELECT * FROM BSBT22_Electives")
rows = cur.fetchall()
print("Newly inserted records:")
for row in rows:
    print(row)

# add 'Credits' column and set default value to 2
cur.execute("ALTER TABLE BSBT22_Electives ADD COLUMN Credits INTEGER DEFAULT 2")

# Verify that the insertions have been effected
cur.execute("PRAGMA table_info(BSBT22_Electives)")
columns = cur.fetchall()
print("Columns in BSBT22_Electives after adding 'Credits' column:")
for column in columns:
    print(column)

# delete the above 4 rows and verify  
cur.execute("DELETE FROM BSBT22_Electives WHERE Elective IN ('Elective1', 'Elective2', 'Elective3', 'Elective4')")
conn.commit()
conn.execute("VACUUM")

# Check the new row counts
cur.execute("SELECT COUNT(*) FROM BSBT22_Electives")
row_count = cur.fetchone()[0]
print("Row count after deletion:", row_count)

# Verify that the deleted records do not display
cur.execute("SELECT * FROM BSBT22_Electives")
rows = cur.fetchall()
print("Records after deletion:")
for row in rows:
    print(row)

# delete Counts column and verify  

conn = lite.connect('BSc22_SEE_alishat.sqlite')
cur = conn.cursor()

# Create a new table without the 'Credits' column
cur.execute("CREATE TABLE BSBT22_Electives_New AS SELECT Elective, Course, Section, Name, Sex, Email FROM BSBT22_Electives")

# Rename the original table
cur.execute("ALTER TABLE BSBT22_Electives RENAME TO BSBT22_Electives_Old")

# Rename the new table to the original table name
cur.execute("ALTER TABLE BSBT22_Electives_New RENAME TO BSBT22_Electives")

# Check the column
cur.execute("PRAGMA table_info(BSBT22_Electives)")
columns = cur.fetchall()
print("Columns in BSBT22_Electives after deleting 'Credits' column:")
for column in columns:
    print(column)

"""---
#### Tasks Level 2   

<pre>
5. Create 3 tables:                                                                                  4
    a) 'Elective' lookup table. Auto-generated primary key and a text type column 'Elective_Name'.  (1) 
    b) 'Course' lookup table. Auto-generated primary key and a text type column 'Course_Name'       (1) 
    c) 'Student' table with columns Name, Sex, USN, Email, Course_ID, Section, and Elective_Id.     (2)
          Constraints: USN as Primary Kay, Course_ID and Elective_Id as Foreign Keys.     
</pre>

##### a. 'Elective' lookup table. Auto-generated primary key and a text type column 'Elective_Name'
"""

# code
sql ="""CREATE TABLE Elective (
  Elective_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Elective_Name TEXT
);"""

"""##### b. 'Course' lookup table. Auto-generated primary key and a text type column 'Course_Name' """

# code
sql = """CREATE TABLE Course (
  Course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Course_Name TEXT
);"""

"""##### c. 'Student' table with columns Name, Sex, USN, Email, Course_ID, Section, and Elective_Id.  
          Constraints: USN as Primary Kay, Course_ID and Elective_Id as Foreign Keys.  
"""

# code
sql ="""CREATE TABLE Student (
  Name TEXT,
  Sex TEXT,
  USN TEXT PRIMARY KEY,
  Email TEXT,
  Course_ID INTEGER,
  Section TEXT,
  Elective_ID INTEGER,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID),
  FOREIGN KEY (Elective_ID) REFERENCES Elective (Elective_ID)
);"""

"""<pre>
6. Insert appropriate data into these tables.                                         4
   You may take data from BSBT22_Electives table or   
   read from ‘BSBT22_Electives.xlsx’   
</pre>

##### Insert rows to Course table
"""

# code
# Create the Course table
cur.execute("""
    CREATE TABLE Course (
        Course_ID INTEGER PRIMARY KEY,
        Name TEXT
    )
""")

# Insert rows into the Course table
cur.execute("INSERT INTO Course (Course_ID, Name) VALUES (1, 'BSc')")
cur.execute("INSERT INTO Course (Course_ID, Name) VALUES (2, 'BTech')")
conn.commit()

"""##### Insert rows to Elective table  """

# code
# Create the Elective table
cur.execute("""
    CREATE TABLE Elective (
        Elective_ID INTEGER PRIMARY KEY,
        Elective_Name TEXT
    )
""")

# Insert rows into the Elective table
cur.execute("INSERT INTO Elective (Elective_Name) VALUES ('Photography')")
cur.execute("INSERT INTO Elective (Elective_Name) VALUES ('Drumming')")
cur.execute("INSERT INTO Elective (Elective_Name) VALUES ('Kuchipudi')")
cur.execute("INSERT INTO Elective (Elective_Name) VALUES ('Quantitative Reasoning')")
conn.commit()

"""##### Insert rows to Student table  
<u>Note</u>: get values for FK columns from Elective and Course tables.     
"""

#code
# Create the Student table
cur.execute("""
    CREATE TABLE Student (
        Name TEXT,
        Sex TEXT,
        USN TEXT PRIMARY KEY,
        Email TEXT,
        Course_ID INTEGER,
        Section TEXT,
        Elective_ID INTEGER,
        FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID),
        FOREIGN KEY (Elective_ID) REFERENCES Elective (Elective_ID)
    )
""")

# FK values from Elective and Course tables
cur.execute("SELECT Elective_ID FROM Elective WHERE Elective_Name = 'Kuchipudi'")
elective_id = cur.fetchone()[0]

cur.execute("SELECT Course_ID FROM Course WHERE Name = 'BSc'")
course_id = cur.fetchone()[0]

# Insert rows into the Student table
cur.execute("INSERT INTO Student (Name, Sex, USN, Email, Course_ID, Section, Elective_ID) VALUES ('John Doe', 'Male', '123456', 'john@example.com', ?, 'A', ?)", (course_id, elective_id))
cur.execute("INSERT INTO Student (Name, Sex, USN, Email, Course_ID, Section, Elective_ID) VALUES ('Jane Smith', 'Female', '789012', 'jane@example.com', ?, 'B', ?)", (course_id, elective_id))

conn.commit()

"""<pre>
7. Investigate the basic structure of the tables.                                   2
   Querying the Student table,  
   print the unique values for  
   Courses, Electives, Sex, and Sections.    
</pre>   
"""

# code
#unique values for Courses
cur.execute("SELECT DISTINCT Course_ID FROM Student")
courses = cur.fetchall()
print("Unique Courses:")
for course in courses:
    print(course[0])

#unique values for Electives
cur.execute("SELECT DISTINCT Elective_ID FROM Student")
electives = cur.fetchall()
print("Unique Electives:")
for elective in electives:
    print(elective[0])

#unique values for Sex
cur.execute("SELECT DISTINCT Sex FROM Student")
sexes = cur.fetchall()
print("Unique Sexes:")
for sex in sexes:
    print(sex[0])

#unique values for Sections
cur.execute("SELECT DISTINCT Section FROM Student")
sections = cur.fetchall()
print("Unique Sections:")
for section in sections:
    print(section[0])

"""<pre>
8. Search, filter, and print data ordered by column(s)                             3
   using relationship across the tables.      
   From Student, Elective, and Course tables,  
   get data for USN, Elective_Name, Course_Name, and Section.  
   Display the results for the complete table.  
</pre>
"""

# code
# Querying the data from the tables
cur.execute("""
    SELECT Student.USN, Elective.Elective_Name, Course.Name, Student.Section
    FROM Student
    JOIN Elective ON Student.Elective_ID = Elective.Elective_ID
    JOIN Course ON Student.Course_ID = Course.Course_ID
""")

# Fetching the results
rows = cur.fetchall()

# Displaying the results
print("USN\tElective Name\tCourse Name\tSection")
for row in rows:
    usn, elective_name, course_name, section = row
    print(f"{usn}\t{elective_name}\t\t{course_name}\t\t{section}")

"""<pre>
9. Search, filter, and print data ordered by column(s) using JOIN on the tables.  3
</pre>
"""

#code

# Add the 'Course_Name' column to the 'Course' table
cur.execute("ALTER TABLE Course ADD COLUMN Course_Name TEXT")

# Update the 'Course_Name' values for existing rows in the table
cur.execute("""
    UPDATE Course
    SET Course_Name = 'BSc' 
    WHERE Course_Id = 1
""")
cur.execute("""
    UPDATE Course
    SET Course_Name = 'BTech'
    WHERE Course_Id = 2
""")

# Commit the changes to the database
conn.commit()

# Querying the data from the tables and ordering by USN
cur.execute("""
    SELECT Student.USN, Elective.Elective_Name, Course.Course_Name, Student.Section
    FROM Student
    JOIN Elective ON Student.Elective_Id = Elective.Elective_Id
    JOIN Course ON Student.Course_Id = Course.Course_Id
    ORDER BY Student.USN
""")

# Fetching the results
rows = cur.fetchall()

# Displaying the results
print("USN\tElective Name\tCourse Name\tSection")
for row in rows:
    usn, elective_name, course_name, section = row
    print(f"{usn}\t{elective_name}\t\t{course_name}\t\t{section}")

"""<pre>
10. Check statistics of features using GROUP BY operation.                        2
   Print values for Elective_Name, Course_Name, Section, and Counts
</pre>
"""

cur.execute("""
    SELECT Elective_Name, Course.Course_Name, Student.Section, COUNT(*) AS Counts
    FROM Student
    INNER JOIN Elective ON Student.Elective_Column_Name = Elective.Elective_Column_Name -- Replace 'Elective_Column_Name' with the actual foreign key column name in the 'Student' and 'Elective' tables
    INNER JOIN Course ON Student.Course_ID = Course.ID -- Replace 'Course_ID' with the actual foreign key column name in the 'Student' and 'Course' tables
    GROUP BY Elective.Elective_Name, Course.Course_Name, Student.Section
""")

# Fetching the results
rows = cur.fetchall()

# Displaying the results
print("Elective Name\tCourse Name\tSection\tCounts")
for row in rows:
    elective_name, course_name, section, counts = row
    print(f"{elective_name}\t\t{course_name}\t\t{section}\t\t{counts}")

"""<pre>
11. Demonstrate the effect of setting PK and FK constraints                       2
    while inserting rows to the child table and 
    while deleting rows from the parent table.  
    Note: you have to set PRAGMA to enable FK constraint. 
</pre>    
"""

# pragma
cur.execute("PRAGMA foreign_keys = ON")

# insert student record with non-existant FK 
cur.execute("INSERT INTO Student (Name, Sex, USN, Email, Course_ID, Section, Elective_Id) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("John Doe", "Female", "1RVU22BSC009", "alishat.bsc22@rvu.edu.in", 999, "A", 9999))

# insert student record with duplicate PK 
cur.execute("INSERT INTO Student (Name, Sex, USN, Email, Course_ID, Section, Elective_Id) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("Alisha Taj", "Female", "1RVU22BSC009", "alishat.bsc22@rvu.edu.in", "C001", "A", 1234))

"""Integrity error so could not do it

"""



# delete a record from Elective 
cur.execute("DELETE FROM Elective WHERE Elective_Id = ?", (elective_id,))