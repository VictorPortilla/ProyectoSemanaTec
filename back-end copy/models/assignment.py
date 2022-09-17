from marshmallow_sqlalchemy import SQLAlchemySchema
from models.shared import db
from models.user_has_assignment import UserHasAssignment

class Assignment(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    due_date=db.Column(db.DateTime,nullable=False)
    description=db.Column(db.String(500),nullable=True)
    completed=db.Column(db.Boolean,nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def save_relation(self):
        db.session.commit()

class AssignmentSchema(SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'due_date', 'description', 'completed')
        model = Assignment
        load_instance = True

