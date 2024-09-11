from django.shortcuts import render
import mysql.connector as sql
from django.http import HttpResponse

# Create your views here.

firstname = ''
lastname = ''
emails = ''
passwords = ''

def signaction(request):
    global firstname, lastname, emails, passwords
    if request.method == "POST":
        try:
            # Establish the MySQL connection
            m = sql.connect(host='localhost', user='root', password='Pd123456@@', database='authlogin')
            cursor = m.cursor()

            # Get form data
            data = request.POST
            for key, value in data.items():
                if key == 'first_name':
                    firstname = value
                if key == 'last_name':
                    lastname = value
                if key == 'email':
                    emails = value
                if key == 'password':
                    passwords = value

            # Insert the data into the 'users' table (adjust the table column names accordingly)
            query = "INSERT INTO users (firstname, lastname, email, passwords) VALUES (%s, %s, %s, %s)"
            values = (firstname, lastname, emails, passwords)

            cursor.execute(query, values)
            m.commit()

            # Return success response or redirect to another page
            return HttpResponse("User created successfully")

        except sql.Error as err:
            # Handle database errors
            return HttpResponse(f"Error: {str(err)}")

    # Render the signup form on GET request
    return render(request, 'signup.html')
