from crypt import methods
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models.assignment import AssignmentSchema,Assignment
from models.classdb import Class, ClassSchema
from models.user import User,UserSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2210@localhost:5454/semana_tec'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return "My API is running"

@app.route('/user/list')
def first_api():
    users=User.query.all()
    user_schema=UserSchema(many=True)
    return user_schema.dumps(users)

@app.route('/user/assignments/<id>')
def get_user_assignments(id):
    user=User.query.filter(User.id==id).first()
    assignments=Assignment.query.filter(Assignment.users.contains(user)).all()
    assignment_schema=AssignmentSchema(many=True)
    return assignment_schema.dumps(assignments)

@app.route('/user/create',methods=['POST'])
def creat_usuario():
    body=request.get_json()
    user_schema=UserSchema()
    user=user_schema.load(body,session=db.session)
    user.save()
    return user_schema.dump(user)
'''
@app.route('/class/create', methods=['POST'])
def create_class():
    body=request.get_json()
    class_schema=ClassSchema()
    Classc = class_schema.load(body,session=db)

'''

@app.route('/assignment/create',methods=['POST'])
def create_assignment():
    body=request.get_json()
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()
    return assignment_schema.dump(assignment)    

@app.route('/assignment/assign',methods=['POST'])
def assign():
    body=request.get_json()
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()
    return assignment_schema.dump(assignment) 
