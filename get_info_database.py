import mysql.connector
def get_info_by_id(student_id):
    
    try:
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="StudentInformation"
        )

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Define the query to retrieve the student information
        query = f"SELECT * FROM student WHERE student_id = {int(student_id)} ;"

        # Execute the query
        cursor.execute(query)

        # Retrieve the result
        result = list(cursor.fetchone())

        # Close the database connection
        db.close()

        if result is None:

            return None
        else:


        # Create a dictionary to hold the student information
            student_info = {
            "Student id": result[0],
            "Name": result[1],
            "Section": result[2],
            "Program": result[3],
            "Year of Admission": result[4]
        } ; 

        # Return the student information
            return student_info
    
    except Exception as e:
        print(f"Error retrieving student information: {e}")
        return None
