import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="StudentInformation"
)


# Create a cursor object to execute queries
cursor = db.cursor()

def save_info(my_info):
    # Check if data already exists in table
    check_query = "SELECT student_id FROM student WHERE student_id = %s"
    cursor.execute(check_query, (my_info['Student id'],))
    result = cursor.fetchone()
    # Commit the transaction

    #Data Already Present
    if result is not  None:
        ans = 0
    
    # Data is Saved
    else:
        # Define the insert query
        insert_query = "INSERT INTO student (student_id, student_name, Department, Program, Year_of_Admission) VALUES (%s, %s, %s, %s, %s)"
        
        # Define the values to insert
        values = (my_info['Student id'], my_info['Name'], my_info['Section'], my_info['Program'], my_info['Year of Admission'])

        # Execute the insert query
        cursor.execute(insert_query, values)
        
        ans = 1

    
    db.commit()
    
    
    return ans
    db.close()
