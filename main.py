from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from flask import Flask,jsonify,request
from db_tables import Session,engine
from datetime import datetime
import os



# Endpoints

app = Flask(__name__)

@app.route("/")
def index():
    return "Startup Page"

@app.route('/residents', methods=['POST'])
def create_resident():
    from db_tables import residentInfo
    local_session = Session(bind=engine)
    residentID = request.json['residentID']
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    password = request.json['password']
    email = request.json['email']

    new_resident = residentInfo(residentID=residentID, firstName=firstName, lastName=lastName, password=password,
                                email=email)
    local_session.add(new_resident)
    local_session.commit()

    return jsonify({'message': 'New user created!'})


@app.route('/residents', methods=['GET'])
def get_residents():
    from db_tables import residentInfo
    local_session = Session(bind=engine)
    residents = local_session.query(residentInfo).all()
    output = []
    for resident in residents:
        resident_data = {}
        resident_data['residentID'] = resident.residentID
        resident_data['firstName'] = resident.firstName
        resident_data['lastName'] = resident.lastName
        resident_data['email'] = resident.email
        output.append(resident_data)

    return jsonify({'residents': output})

@app.route('/login', methods=['POST'])
def login():
    from db_tables import residentInfo
    local_session = Session(bind=engine)
    email = request.json.get('email')
    password = request.json.get('password')
    resident = local_session.query(residentInfo).filter_by(email=email).first()

    if resident and resident.password == password:
        return jsonify({'message': 'Successfully logged in!'})

    return jsonify({'error': 'Invalid email or password'})

if __name__=="__main__":
    app.run(debug=True)