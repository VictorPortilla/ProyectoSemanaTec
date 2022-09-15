from models.shared import db
UserHasAssignment = db.Table("user_has_assignment",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("assignment_id", db.Integer, db.ForeignKey("assignment.id")),
)

