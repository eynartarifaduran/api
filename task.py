from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.String(20), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)
