from flask import Flask, request, jsonify
app = Flask(__name__)
doctors = {}
patients = {}
appointments = {}
doctor_id = 1
patient_id = 1
appointment_id = 1


# Create Doctor
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    global doctor_id
    data = request.json
    data["doctor_id"] = doctor_id
    doctors[doctor_id] = data
    doctor_id += 1
    return jsonify(data), 201


# Register Patient
@app.route("/v1/patients", methods=["POST"])
def create_patient():
    global patient_id
    data = request.json

    if data.get("age", 0) < 0:
        return {"error": "Invalid age"}, 400

    if "email" not in data:
        return {"error": "Email required"}, 400

    data["patient_id"] = patient_id
    patients[patient_id] = data
    patient_id += 1

    return jsonify(data), 201


#  Book Appointment
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    global appointment_id
    data = request.json
    for appt in appointments.values():
        if (appt["doctor_id"] == data["doctor_id"] and
            appt["date"] == data["date"] and
            appt["time"] == data["time"]):
            return {"error": "Slot already booked"}, 409

    data["appointment_id"] = appointment_id
    appointments[appointment_id] = data
    appointment_id += 1

    return jsonify(data), 201


#  Get Appointment
@app.route("/v1/appointments/<int:id>", methods=["GET"])
def get_appointment(id):
    if id not in appointments:
        return {}, 404
    return jsonify(appointments[id])


# Reschedule
@app.route("/v1/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):
    if id not in appointments:
        return {}, 404

    new_data = request.json

    for aid, appt in appointments.items():
        if aid != id and appt["doctor_id"] == appointments[id]["doctor_id"] \
           and appt["date"] == new_data["date"] and appt["time"] == new_data["time"]:
            return {"error": "Slot already booked"}, 409

    appointments[id].update(new_data)
    return jsonify(appointments[id])


# Cancel
@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):
    if id not in appointments:
        return {}, 410

    del appointments[id]
    return "", 204


app.run(debug=True)