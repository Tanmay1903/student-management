from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)

    student = db.relationship('Student', backref=db.backref('scores', lazy=True))

# Routes
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    try:
        new_student = Student(name=data['name'], student_id=data['student_id'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": f"Student {data['name']} added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Student already exists!"}), 400

@app.route('/scores', methods=['POST'])
def add_score():
    data = request.json
    student = Student.query.filter_by(name=data['student_name']).first()
    if not student:
        return jsonify({"message": "Student not found!"}), 404

    new_score = Score(student_id=student.student_id, subject=data['subject'], score=data['score'])
    db.session.add(new_score)
    db.session.commit()
    return jsonify({"message": f"Score of {data['score']} added for {data['student_name']} in {data['subject']}."}), 201

@app.route('/students/<name>/subject', methods=['GET'])
def get_subject(name):
    student = Student.query.filter_by(name=name).first()
    if not student:
        return jsonify({"message": "Student not found!"}), 404

    subjects = ",".join([score.subject for score in student.scores])
    return jsonify({"subjects": subjects}), 200

@app.route('/scores/summary', methods=['GET'])
def summarize_scores():
    subject = request.args.get('subject')
    scores = Score.query.filter_by(subject=subject).all()

    if not scores:
        return jsonify({"summary": f"No scores available for {subject}."}), 404

    avg_score = sum([score.score for score in scores]) / len(scores)
    return jsonify({"summary": f"Average score for {subject} is {avg_score}."}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5051)
