import os
from flask import request, jsonify,Flask,render_template,session,redirect,url_for
import random
from views.customer import customerView
from views.reservation import reservationView
from views.admin import adminView

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_customer', methods=['GET'])
def new_customer_form():
    return render_template('new_customer.html')

@app.route('/existing_user')
def existing_user():
    return render_template('existing_user.html')

@app.route('/make_reservation', methods=['GET'])
def make_reservation():
    user_data = session.get('user_data')
    if user_data:
        return render_template('reservation.html', user_data=user_data)
    else:
        return redirect(url_for('login')) 

@app.route('/api/new_customer', methods=['POST'])
def add_customer():
    customerId=random.randint(1000,9999),
    username=request.form.get('username'),
    name=request.form.get('name'),
    address=request.form.get('address'),
    phoneNumber=request.form.get('phone_number'),
    email=request.form.get('email')
    customer = customerView(
    customerId[0],
    username[0],
    name[0],
    address[0],
    phoneNumber[0],
    email
    )
    session['user_data'] = {
            "username": username[0],
            "name": name[0],
            "email": email,
            "phone_number": phoneNumber[0]
        }
    result_msg=customer.insert()
    return redirect(url_for('make_reservation'))

@app.route('/login', methods=['POST'])
def login():
    customer = customerView(username=request.form.get('username'))
    user=customer.find()

    if user:
        session['user_data'] = {
            "username": user["username"],
            "name": user.get("name", ""),
            "email": user.get("email", ""),
            "phone_number": user.get("phone_number", "")
        }
        return redirect(url_for('make_reservation'))
    else:
        # User does not exist, return an error message
        return jsonify({"error": "User not found"})
    
@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    username=request.form['username'],
    reservationId=random.randint(10000,99999),
    number_of_seats=request.form['number_of_seats'],
    reservation_date=request.form['reservation_date']
    reservation = reservationView(
        username[0],
        reservationId[0],
        number_of_seats[0],
        reservation_date
    )
    result_msg=reservation.insert()
    if result_msg['success']:
        return render_template('reservation_success.html', reservationId=reservationId[0])
    else:
        return jsonify(result_msg)
    
@app.route('/admin/dashboard')
def admin_dashboard():
    admin=adminView()
    return render_template('admin_dashboard.html', customer_reservations=admin.adminData())


if __name__ == '__main__':
    app.run(debug=True)
