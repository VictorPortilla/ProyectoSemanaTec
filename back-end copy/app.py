from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models.assignment import AssignmentSchema,Assignment
from models.classdb import Class,ClassSchema
from models.user import User,UserSchema
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required, current_identity
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jwawlcebwmdinf:ab8c18bcf47a2374d5b4fb3a0f5a0e8af75ab0acaac38db3d2a467eaf78f444b@ec2-34-231-42-166.compute-1.amazonaws.com:5432/d2ko9tna94o8d'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'super-secret'

def authenticate(username, password):
    user = User.query.filter(User.email==username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id==user_id).first()

jwt = JWT(app, authenticate, identity)

@app.route('/')
def hello_world():
    return "My API is running"

@app.route('/user/list') #Te da los usuarios en la db
def first_api():
    users=User.query.all()
    user_schema=UserSchema(many=True)
    return user_schema.dumps(users)

@app.route('/user/assignments/<id>') #Te da las tareas de un usuario
def get_user_assignments(id):
    user=User.query.filter(User.id==id).first()
    assignments=Assignment.query.filter(Assignment.users.contains(user)).all()
    assignment_schema=AssignmentSchema(many=True)
    return assignment_schema.dumps(assignments)

@app.route('/user/create',methods=['POST']) #Crea usuario
def creat_usuario():
    body=request.get_json()
    body["password"]=bcrypt.generate_password_hash(body["password"])
    user_schema=UserSchema()
    user=user_schema.load(body,session=db.session)
    user.save()
    return user_schema.dump(user)

@app.route('/class/create', methods=['POST']) #Crea una clase y asigna la clase a un arreglo de usuarios
@jwt_required()
def create_class():
    body=request.get_json()
    userList = body.pop('users')
    class_schema=ClassSchema()
    Classdb= class_schema.load(body,session=db.session)
    Classdb.save()
    #iteramos sobre userList, guardando cada relación 
    #userList[0].assigments.append(assignment.id)
    currentClass = Class.query.filter_by(id=Classdb.id).first()
    for userID in userList:
        currentUser = User.query.filter_by(id=userID).first()
        currentClass.users.append(currentUser)
    currentClass.save_relation()
    return class_schema.dump(Classdb)

@app.route('/class/users/<id>') #Te da los usuarios de una clase
def get_class_users(id):
    classdb=Class.query.filter(Class.id==id).first()
    user=User.query.filter(User.classes.contains(classdb)).all()
    user_schema = UserSchema(many=True)
    return user_schema.dumps(user)

@app.route('/user/classes/<id>') #Te da las clases de un usuario
def get_user_classes(id):
    user=User.query.filter(User.id==id).first()
    classdb=Class.query.filter(Class.users.contains(user)).all()
    class_schema = ClassSchema(many=True)
    return class_schema.dumps(classdb)

@app.route('/assignment/create',methods=['POST'])
@jwt_required()
def create_assignment():
    body=request.get_json()
    #body es un dict
    userList = body.pop('users')
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()

    #iteramos sobre userList, guardando cada relación 
    #userList[0].assigments.append(assignment.id)
    currentAssignment =  Assignment.query.filter_by(id=assignment.id).first()
    for userID in userList:
        currentUser = User.query.filter_by(id=userID).first()
        #if user: #no tendriamos que, pues solo damos opciones validas
        currentAssignment.users.append(currentUser)

    currentAssignment.save_relation()
    return assignment_schema.dump(assignment)

@app.route('/assignment/complete', methods=['POST'])
@jwt_required()
def complete_assignment():
    body=request.get_json()
    assignment = Assignment.query.filter_by(id=body['id']).first()
    assignment.completed = True
    assignment.save()
    return AssignmentSchema().dump(assignment)

@app.route('/assignment/assign',methods=['POST'])
@jwt_required()
def assign():
    body=request.get_json()
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()
    return assignment_schema.dump(assignment) 

@app.route('/protected')
@jwt_required()
def protected():
    user_schema=UserSchema()
    return '%s' % user_schema.dump(current_identity)
