from flask import Flask, render_template, request, flash, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-123')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name')
        email   = request.form.get('email')
        message = request.form.get('message')
        print(f"New enquiry from {name} ({email}): {message}")
        flash('Thank you! We will contact you shortly.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)