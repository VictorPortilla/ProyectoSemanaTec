from marshmallow_sqlalchemy import SQLAlchemySchema
from models.shared import db
from models.user_has_assignment import UserHasAssignment

class Class(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name=db.Column(db.String(100),nullable=False)
    professor = db.column(db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    

class AssignmentSchema(SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'professor')
        model = Class
        load_instance = True
