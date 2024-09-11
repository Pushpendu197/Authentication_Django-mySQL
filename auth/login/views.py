from django.shortcuts import render
import mysql.connector as sql

emails = ''
passwords = ''

def loginaction(request):
    global emails, passwords
    if request.method == "POST":
        # Establish the MySQL connection
        m = sql.connect(host='localhost', user='root', password='Pd123456@@', database='authlogin')
        cursor = m.cursor()

        # Get form data
        data = request.POST
        for key, value in data.items():
            if key == 'email':
                emails = value
            if key == 'password':
                passwords = value

        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE email=%s AND passwords=%s"
        cursor.execute(query, (emails, passwords))
        t = tuple(cursor.fetchall())

        # Check if the query returned any results
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, "welcome.html")

    return render(request, 'login.html')
