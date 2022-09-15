from marshmallow_sqlalchemy import SQLAlchemySchema
from models.shared import db
from models.class_has_user import ClassHasUser

class Class(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(100),nullable=False)
    professor = db.Column(db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    

class ClassSchema(SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'professor')
        model = Class
        load_instance = True