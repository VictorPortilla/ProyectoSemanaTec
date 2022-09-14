from models.shared import db
ClassHasUser = db.Table(
    "class_has_user",
    db.Column("class_id", db.ForeignKey("class.id")),
    db.Column("user_id", db.ForeignKey("user.id")),
    
)