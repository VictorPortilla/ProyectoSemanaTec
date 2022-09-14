from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.shared import db
from models.assignment import Assignment, AssignmentSchema
from models.classdb import Class, ClassSchema
from marshmallow_sqlalchemy.fields import Nested
from models.user_has_assignment import UserHasAssignment
from models.class_has_user import ClassHasUser
from sqlalchemy.orm import relationship

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    assignments = relationship('Assignment', secondary=UserHasAssignment,viewonly=True, backref='User')
    classes = relationship('Class', secondary=ClassHasUser,viewonly=True, backref='User')

    def save(self):
        db.session.add(self)
        db.session.commit()

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        assignments = Nested(AssignmentSchema, many=True, allow_null=True, default=None)
        classes = Nested(ClassSchema, many=True, allow_null=True, default=None)