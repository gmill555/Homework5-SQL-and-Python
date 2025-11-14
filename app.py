from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)


def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Oreo2023!",
            database="db_registra"
        )
    except Error as e:
        print("MySQL connection error:", e)
        return None

@app.route('/', methods=['GET', 'POST'])
def register_student():
    message = ""
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birth_date = request.form.get('birth_date')
        email = request.form.get('email')

        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO tbl_student (first_name, last_name, birth_date, email) VALUES (%s,%s,%s,%s)",
                    (first_name, last_name, birth_date, email)
                )
                conn.commit()
                cursor.close()
                message = "Student Registered Successfully!"
            except Error as e:
                message = f"Database Error: {e}"
            finally:
                conn.close()
        else:
            message = "Could not connect to the database."

    return render_template('form.html', message=message)

if __name__ == '__main__':
    print("Templates folder:", app.template_folder)
    app.run(debug=True)
