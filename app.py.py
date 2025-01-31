from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Route to display the contact form
@app.route('/')
def contact_form():
    return render_template('contact_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get data from the form
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Save data to SQLite database
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contact (name, email, message) 
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

