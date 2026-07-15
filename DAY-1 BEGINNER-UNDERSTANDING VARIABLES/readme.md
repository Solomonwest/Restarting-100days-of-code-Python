# Flask + MySQL CRUD Web App Tutorial

## Objective
Build a simple CRUD web app where users can add, view, update and delete students.

## Fields
- Name
- Email
- Matric Number
- Department
- Faculty

## Setup
```bash
python -m venv venv
# activate
pip install flask flask-mysqldb
```

## Database
Start the Local Servers Before accessing the database dashboard, you must run the background database services.

### Step 1 Starting DB Services
#### For XAMPP Users:

- Open the XAMPP Control Panel application on your computer.
- Click the Start button next to Apache.
- Click the Start button next to MySQL.
- Ensure both modules turn green, 
- indicating they are active.

### For WAMP Users:
- Launch the WampServer application.
- Look for the W icon in your Windows system tray (bottom right corner).
- Wait for the icon to turn completely Green (Red means stopped, Orange means partial).

### Step 2 Starting PHPMyAdmin
- Open phpMyAdminOpen your preferred web browser (e.g., Chrome, Edge, Firefox).
- Type http://localhost/phpmyadmin into the address bar and press Enter.
- Note for WAMP users: If a login screen appears, type root as the username and leave the password field completely blank, then click Go. 

### Step 3: Create Your Database
- Once the phpMyAdmin interface loads, follow these universal steps for both platforms:
  - Click on the Databases tab located in the top-left menu bar.
  - Find the text box labeled Create database.
  - Type a name for your database (e.g., my_first_db). 
  - Avoid spaces or special characters. Use underscores if needed.
  - Leave the dropdown menu next to it on the default setting (usually utf8mb4_general_ci).
  - Click the Create button.

### Step 4: Creating you database table
- Click on the SQL tab
- Paste the following code and click Go

```sql
CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),email VARCHAR(100),matric_number VARCHAR(30),department VARCHAR(100),faculty VARCHAR(100));
```
- You are done with your database setup
- Leave everything running as you continue the python sections

## Project Structure
- This section should be in you IDE (PyCharm, VsCode, whichever)
```text
student_crud/
 app.py
 templates/
  index.html
  add.html
  edit.html
```

## app.py
Copy and paste the following starter code and complete the CRUD routes.

```python
from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
# configure MySQL then implement:
# / -> list students
# /add -> insert student
# /edit/<id> -> update student
# /delete/<id> -> delete student
app.run(debug=True)
```

## index.html
```html
Display all students in a table with Edit and Delete links and an Add Student button.
```

## add.html
```html
Create a form with Name, Email, Matric Number, Department and Faculty.
```

## edit.html
```html
Reuse the same form and prefill the existing values.
```

## Run
```bash
python app.py
```

# Complete Flask + MySQL CRUD

## app.py

```python
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password" #Leave blank if you did not password your DB during creation
app.config["MYSQL_DB"] = "student_db" #This should match the database name from phpMyAdmin

mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students(name,email,matric_number,department,faculty) VALUES(%s,%s,%s,%s,%s)",
            (
                request.form["name"],
                request.form["email"],
                request.form["matric_number"],
                request.form["department"],
                request.form["faculty"],
            ),
        )
        mysql.connection.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    cur = mysql.connection.cursor()
    if request.method == "POST":
        cur.execute(
            "UPDATE students SET name=%s,email=%s,matric_number=%s,department=%s,faculty=%s WHERE id=%s",
            (
                request.form["name"],
                request.form["email"],
                request.form["matric_number"],
                request.form["department"],
                request.form["faculty"],
                id,
            ),
        )
        mysql.connection.commit()
        return redirect("/")
    cur.execute("SELECT * FROM students WHERE id=%s",(id,))
    student=cur.fetchone()
    return render_template("edit.html",student=student)

@app.route("/delete/<int:id>")
def delete(id):
    #implement delete route
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
```

## templates/index.html

```html
<!DOCTYPE html>
<html><body>
<h2>Students</h2>
<a href="/add">Add Student</a>
<table border="1">
<tr><th>Name</th><th>Email</th><th>Matric</th><th>Department</th><th>Faculty</th><th>Action</th></tr>
{% for s in students %}
<tr>
<td>{{ s[1] }}</td><td>{{ s[2] }}</td><td>{{ s[3] }}</td>
<td>{{ s[4] }}</td><td>{{ s[5] }}</td>
<td><a href="/edit/{{ s[0] }}">Edit</a> | <a href="/delete/{{ s[0] }}">Delete</a></td>
</tr>
{% endfor %}
</table>
</body></html>
```

## templates/add.html

```html
<!DOCTYPE html>
<html><body>
<h2>Add Student</h2>
<form method="POST">
<input name="name" placeholder="Name"><br>
<input name="email" type="email" placeholder="Email"><br>
<input name="matric_number" placeholder="Matric Number"><br>
<input name="department" placeholder="Department"><br>
<input name="faculty" placeholder="Faculty"><br>
<button type="submit">Save</button>
</form>
</body></html>
```

## templates/edit.html

```html
<!DOCTYPE html>
<html><body>
<h2>Edit Student</h2>
<form method="POST">
<input name="name" value="{{ student[1] }}"><br>
<input name="email" value="{{ student[2] }}"><br>
<input name="matric_number" value="{{ student[3] }}"><br>
<input name="department" value="{{ student[4] }}"><br>
<input name="faculty" value="{{ student[5] }}"><br>
<button>Update</button>
</form>
</body></html>
```

## Exercise
- Figure out how to run the application (A command in the terminal/CLI)
- Complete the delete route.