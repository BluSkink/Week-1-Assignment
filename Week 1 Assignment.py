# Flask Library
from flask import Flask, request, jsonify

# Create App Object
app = Flask(__name__)

# List of Students
students = [
    {
        "id": 1,
        "name": 'tom'
    },
    {
        "id": 2,
        "name": "Jerry"
    },
    {
        "id": 3,
        "name": "Bugs Bunny"
    }
]

# Example endpoint
@app.route('/example')
def home():
    return "Welcome to the Flask API!"

#### ASSIGNMENT STARTS HERE ####

# GET all students
@app.route('/', methods=['GET'])
def get_all_students():
    return jsonify(students), 200

# GET student by ID
@app.route('/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

# POST - Add new student
@app.route('/', methods=['POST'])
def add_student():
    new_student = request.get_json()
    if "id" not in new_student or "name" not in new_student:
        return jsonify({"error": "Invalid data"}), 400

    if any(s["id"] == new_student["id"] for s in students):
        return jsonify({"error": "Student ID already exists"}), 400

    students.append(new_student)
    return jsonify(new_student), 201

# PUT - Update student by ID
@app.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_data = request.get_json()
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    if "name" in updated_data:
        student["name"] = updated_data["name"]
        return jsonify(student), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

# DELETE - Delete student by ID
@app.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"}), 200

#### ASSIGNMENT ENDS HERE ####

if __name__ == '__main__':
    app.run(debug=True)
