from flask import Flask, jsonify
app = Flask(__name__)

instructors = [
    { 'firstName': "Muhammad", 'lastName': "Sannan"  }
]
students = [
    { 'id': "1", 'firstName': "test", 'lastName': "Mbooh"  },
    { 'id': "2",'firstName': "Jose", 'lastName': "Ugorji"  }
]

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/instructors', methods=["GET"])
def getInstructors():
    return jsonify(instructors)

@app.route('/students', methods=["GET"])
def getStudents():
    return jsonify(students)

@app.route('/instructor/<id>', methods=["GET"])
def getInstructor(id):
    id = int(id) - 1
    return jsonify(instructors[id])

@app.route('/student/<id>', methods=["GET"])
def getStudent(id):
    id = int(id) - 1
    return jsonify(students[id])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
