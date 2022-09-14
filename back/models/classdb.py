from marshmallow_sqlalchemy import SQLAlchemySchema
from models.shared import db
from models.class_has_user import ClassHasUser

class Class(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name=db.Column(db.String(100),nullable=False)
    professor = db.column(db.String(100), nullable=False)
    users = db.relationship('User', secondary = 'class_has_user')

    def save(self):
        db.session.add(self)
        db.session.commit()
    

class ClassSchema(SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'professor')
        model = Class
        load_instance = True
