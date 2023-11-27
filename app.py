# Import necessary modules
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the app to use a MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://brightonomondi:passbright@localhost/dbname'
db = SQLAlchemy(app)

# Define a model for the 'Booking' table in the database
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)       # Unique identifier for each booking
    name = db.Column(db.String(80), nullable=False)     # Name of the person making the booking
    email = db.Column(db.String(120), nullable=False)    # Email address of the person
    phone_number = db.Column(db.String(20), nullable=False)  # Phone number of the person

# Define a route for the homepage
@app.route('/')
def index():
    return render_template('aboutme.html')  # Render an 'aboutme.html' template for the homepage

# Define a route for submitting booking information
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Extract data from the form submitted by the user
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']

        # Create a new booking entry in the database
        booking = Booking(name=name, email=email, phone_number=phone_number)
        db.session.add(booking)
        db.session.commit()

        return "Thank you for booking a meeting, we will get back to you shortly"  # Display a thank you message

if __name__ == '__main__':
    # Create the 'Booking' table in the database if it doesn't exist
    db.create_all()
    app.run(debug=True)  # Start the Flask app in debug mode if this script is run directly
